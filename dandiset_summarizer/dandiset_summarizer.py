#!/usr/bin/env python

from typing import List
import os
import json
import time
import urllib.request
import click
from pydantic import BaseModel
import dandi.dandiarchive as da
import lindi
import openai


thisdir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(thisdir)

def dandiset_summarizer(*, dandiset_id: str, dandiset_version: str, cache_dir: str, gpt_model: str):
    dandiset_dir = f'{parent_dir}/dandisets/{dandiset_id}'
    summary_md_fname = f'{dandiset_dir}/summary.md'
    if os.path.exists(summary_md_fname):
        raise Exception(f"Summary already exists at {summary_md_fname}.")
    dandiset_raw_metadata = _get_raw_metadata_for_dandiset(dandiset_id=dandiset_id)

    asset_objects = _get_asset_objects_for_dandiset(
        dandiset_id=dandiset_id, dandiset_version=dandiset_version, cache_dir=cache_dir
    )

    neurodata_summaries = []
    for asset_index, asset in enumerate(asset_objects):
        lindi_fname = _get_local_lindi_file(
            dandiset_id=dandiset_id,
            asset_index=asset_index,
            asset_id=asset["identifier"],
            asset_path=asset["path"],
            url=asset["download_url"],
            cache_dir=cache_dir,
        )
        with lindi.LindiH5pyFile.from_lindi_file(lindi_fname) as f:
            neurodata_summary = _get_neurodata_summary(f)
            neurodata_summaries.append(neurodata_summary)

    clusters = _cluster_summaries(neurodata_summaries)

    if len(clusters) > 8:
        print('Using only first 8 clusters...')
        clusters = clusters[:8]

    representative_lindi_fnames = [
        _get_local_lindi_file(
            dandiset_id=dandiset_id,
            asset_index=cluster[0],
            asset_id=asset_objects[cluster[0]]["identifier"],
            asset_path=asset_objects[cluster[0]]["path"],
            url=asset_objects[cluster[0]]["download_url"],
            cache_dir=cache_dir,
        )
        for cluster in clusters
    ]
    print('Creating summary prompt...')
    prompt = _create_cluster_summary_prompt(
        dandiset_id=dandiset_id,
        representative_lindi_fnames=representative_lindi_fnames,
        cluster_sizes=[len(cluster) for cluster in clusters],
        dandiset_raw_metadata=dandiset_raw_metadata,
    )
    print('Creating summary...')
    summary = _create_summary_from_prompt(prompt, gpt_model=gpt_model)

    print('Writing summary...')
    if not os.path.exists(dandiset_dir):
        os.makedirs(dandiset_dir)
    summary_prompt_fname = f'{dandiset_dir}/summary_prompt.md'
    embeddings_fname = f'{dandiset_dir}/embeddings.json'
    if os.path.exists(embeddings_fname):
        os.remove(embeddings_fname)
    with open(summary_prompt_fname, "w") as f:
        f.write(prompt)
    with open(summary_md_fname, "w") as f:
        f.write(summary)

    print(f"Summary written to {summary_md_fname}.")


def _create_summary_from_prompt(prompt: str, gpt_model: str):
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise Exception("OPENAI_API_KEY environment variable not set.")
    client = openai.Client(
        api_key=OPENAI_API_KEY,
    )
    chat_completion = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    resp = chat_completion.choices[0].message.content
    if resp is None:
        raise Exception("Failed to generate summary.")
    resp = remove_markdown_code_block_markers(resp)
    return resp


def remove_markdown_code_block_markers(s: str):
    lines = s.split("\n")
    new_lines = []
    in_markdown_code_block = False
    for line in lines:
        if line.startswith("```markdown"):
            in_markdown_code_block = True
            continue
        elif line.startswith("```"):
            if in_markdown_code_block:
                in_markdown_code_block = False
                continue
        new_lines.append(line)
    return "\n".join(new_lines)


def _create_cluster_summary_prompt(
    *,
    dandiset_id: str,
    representative_lindi_fnames: List[str],
    cluster_sizes: List[int],
    dandiset_raw_metadata: dict,
):
    total_num_nwb_files = sum(cluster_sizes)
    txt_lines = []

    txt_lines.append('''
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in a couple paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.
''')

    txt_lines.append("")

    for k, v in dandiset_raw_metadata.items():
        if k in [
            'id',
            'name',
            'contributor',
            'description',
            'assetsSummary',
        ]:
            txt_lines.append(f"{k}: {v}")

    txt_lines.append("")

    txt_lines.append(f"Dandiset {dandiset_id} has {total_num_nwb_files} NWB files.")
    for i, fname in enumerate(representative_lindi_fnames):
        txt_lines.append(f"{cluster_sizes[i]} of these NWB files are of type {i + 1}.")
    txt_lines.append("")
    for i, fname in enumerate(representative_lindi_fnames):
        txt_lines.append("")
        txt_lines.append(f"Here is a summary of the type {i + 1} NWB files:")
        with lindi.LindiH5pyFile.from_lindi_file(fname) as f:
            txt0 = _get_detailed_summary_text_for_lindi_file(f)
            for line0 in txt0.split("\n"):
                txt_lines.append(f"  {line0}")
        txt_lines.append("")
    return "\n".join(txt_lines)


def _get_detailed_summary_text_for_lindi_file(lindi_file: lindi.LindiH5pyFile):
    txt_lines = []

    def process_group(path: str):
        grp = lindi_file[path]
        assert isinstance(grp, lindi.LindiH5pyGroup)
        if "neurodata_type" in grp.attrs:
            description = grp.attrs.get("description", "")
            txt_lines.append(
                f"Group {path} ({grp.attrs['neurodata_type']}) {description}"
            )
        for name in grp:
            if isinstance(grp[name], lindi.LindiH5pyGroup):
                process_group(_join(path, name))
            elif isinstance(grp[name], lindi.LindiH5pyDataset):
                process_dataset(_join(path, name))

    def process_dataset(path: str):
        ds = lindi_file[path]
        assert isinstance(ds, lindi.LindiH5pyDataset)
        if "neurodata_type" in ds.attrs:
            description = ds.attrs.get("description", "")
            txt_lines.append(
                f"Dataset {path} ({ds.attrs['neurodata_type']}) {description} | shape = {ds.shape} | dtype = {ds.dtype}"
            )
        parts = path.split("/")
        if len(parts) == 2:
            # top-level dataset
            val = ds[()]
            txt_lines.append(f"{parts[1]}: {val}")
        if len(parts) == 3 and parts[1] == "general":
            # general dataset
            val = ds[()]
            txt_lines.append(f"{parts[2]}: {val}")

    process_group("/")
    return "\n".join(txt_lines)


def _cluster_summaries(neurodata_summaries: List[str]):
    dist_matrix = _compute_dist_matrix(neurodata_summaries)
    cluster_labels = [i for i in range(1, len(neurodata_summaries) + 1)]
    something_changed = True
    while something_changed:
        something_changed = False
        for i in range(len(neurodata_summaries)):
            for j in range(i + 1, len(neurodata_summaries)):
                if dist_matrix[i][j] == 0:
                    if cluster_labels[i] != cluster_labels[j]:
                        cluster_labels[j] = cluster_labels[i]
                        something_changed = True
    unique_labels = list(set(cluster_labels))
    clusters = []
    for label in unique_labels:
        cluster = []
        for i in range(len(neurodata_summaries)):
            if cluster_labels[i] == label:
                cluster.append(i)
        clusters.append(cluster)
    return clusters


def _compute_dist_matrix(neurodata_summaries: List[str]):
    dist_matrix = []
    for i in range(len(neurodata_summaries)):
        row = []
        for j in range(len(neurodata_summaries)):
            row.append(
                _compute_string_dist(neurodata_summaries[i], neurodata_summaries[j])
            )
        dist_matrix.append(row)
    return dist_matrix


def _compute_string_dist(s1: str, s2: str):
    if s1 == s2:
        return 0
    return 1


def _get_asset_objects_for_dandiset(dandiset_id: str, dandiset_version: str, cache_dir: str):
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    if not os.path.exists(f"{cache_dir}/dandiset_asset_objects"):
        os.makedirs(f"{cache_dir}/dandiset_asset_objects")
    fname = f"{cache_dir}/dandiset_asset_objects/{dandiset_id}.json"
    if os.path.exists(fname):
        mtime = os.path.getmtime(fname)
        if time.time() - mtime < 60 * 60:
            with open(fname, "r") as f:
                return json.load(f)
        else:
            print(f"Removing {fname}...")
            os.remove(fname)
    print(f"Creating {fname}...")
    parsed_url = da.parse_dandi_url(f"https://dandiarchive.org/dandiset/{dandiset_id}/{dandiset_version}/")
    asset_objects = []
    with parsed_url.navigate() as (client, dandiset, assets):
        if dandiset is None:
            raise Exception(f"Dandiset {dandiset_id} not found.")
        num_consecutive_non_nwb = 0
        for asset_obj in dandiset.get_assets("path"):
            asset_path = asset_obj.path
            if not asset_path.endswith(".nwb"):
                num_consecutive_non_nwb += 1
                if num_consecutive_non_nwb >= 100:
                    raise Exception(
                        f"Found {num_consecutive_non_nwb} consecutive non-NWB files. Stopping."
                    )
                continue
            asset = {
                "identifier": asset_obj.identifier,
                "path": asset_path,
                "size": asset_obj.size,
                "download_url": asset_obj.download_url,
                "dandiset_id": dandiset_id,
            }
            asset_objects.append(asset)
            if len(asset_objects) >= 100:
                print("Stopping at 100 assets.")
                break
    with open(fname, "w") as f:
        json.dump(asset_objects, f)
    return asset_objects


def _get_raw_metadata_for_dandiset(dandiset_id: str):
    parsed_url = da.parse_dandi_url(f"https://dandiarchive.org/dandiset/{dandiset_id}")
    with parsed_url.navigate() as (client, dandiset, assets):
        if dandiset is None:
            raise Exception(f"Dandiset {dandiset_id} not found.")
        return dandiset.get_raw_metadata()


def _get_neurodata_summary(lindi_file: lindi.LindiH5pyFile):
    txt_lines = []

    def process_group(path: str):
        grp = lindi_file[path]
        assert isinstance(grp, lindi.LindiH5pyGroup)
        if "neurodata_type" in grp.attrs:
            txt_lines.append(f"{path}: {grp.attrs['neurodata_type']}")
        for name in grp:
            if isinstance(grp[name], lindi.LindiH5pyGroup):
                process_group(_join(path, name))
            elif isinstance(grp[name], lindi.LindiH5pyDataset):
                process_dataset(_join(path, name))

    def process_dataset(path: str):
        ds = lindi_file[path]
        assert isinstance(ds, lindi.LindiH5pyDataset)
        if "neurodata_type" in ds.attrs:
            txt_lines.append(f"{path}: {ds.attrs['neurodata_type']}")

    process_group("/")
    return "\n".join(txt_lines)


def _join(path: str, name: str):
    if path == "/":
        return f"/{name}"
    return f"{path}/{name}"


def _get_local_lindi_file(*, dandiset_id: str, asset_id: str, asset_index: int, asset_path: str, url: str, cache_dir: str):
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    if not os.path.exists(f"{cache_dir}/assets"):
        os.makedirs(f"{cache_dir}/assets")
    lindi_fname = f"{cache_dir}/assets/{asset_id}.lindi.json"
    if not os.path.exists(lindi_fname):
        file_key = f'dandi/dandisets/{dandiset_id}/assets/{asset_id}/nwb.lindi.json'
        lindi_json_url = f'https://lindi.neurosift.org/{file_key}'
        try:
            print(f"[{dandiset_id} {asset_index}] Trying lindi download for {asset_path}...")
            _download_lindi_file(url=lindi_json_url, lindi_fname=lindi_fname)
        except Exception:
            print(f"[{dandiset_id} {asset_index}] Creating lindi file for {asset_path}...")
            with lindi.LindiH5pyFile.from_hdf5_file(url) as lindi_file:
                lindi_file.write_lindi_file(lindi_fname)
    return lindi_fname


def _download_lindi_file(*, url: str, lindi_fname: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        with open(lindi_fname, "wb") as f:
            f.write(response.read())


def do_create_embeddings():
    dirs = [
        f"{parent_dir}/dandisets/{dandiset_id}"
        for dandiset_id in os.listdir(f"{parent_dir}/dandisets")
    ]
    all_embeddings = {}
    for dandiset_dir in dirs:
        dandiset_id = os.path.basename(dandiset_dir)
        summary_md_fname = f"{dandiset_dir}/summary.md"
        if not os.path.exists(summary_md_fname):
            print(f"Summary does not exist for {dandiset_id}.")
            os.rename(dandiset_dir, f"{dandiset_dir}_rm")
            continue
        embeddings_fname = f"{dandiset_dir}/embeddings.json"
        embeddings_obj = {}
        if os.path.exists(embeddings_fname):
            with open(embeddings_fname, "r") as f:
                embeddings_obj = json.load(f)
        # model_name = 'text-embedding-3-small'
        model_name = 'text-embedding-3-large'
        if model_name in embeddings_obj:
            print(f"Embedding for {summary_md_fname} already exist.")
        else:
            print(f"Creating embedding for {summary_md_fname}...")
            with open(summary_md_fname, "r") as f:
                summary = f.read()
            embedding0 = _create_embedding_for_summary(
                summary,
                model=model_name
            )
            x = {
                model_name: embedding0,
            }
            with open(embeddings_fname, "w") as f:
                json.dump(x, f)
        with open(embeddings_fname, "r") as f:
            embeddings_obj = json.load(f)
        all_embeddings[dandiset_id] = embeddings_obj
    with open(f"{parent_dir}/embeddings.json", "w") as f:
        json.dump(all_embeddings, f, indent=2)


def _create_embedding_for_summary(summary: str, *, model: str):
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise Exception("OPENAI_API_KEY environment variable not set.")
    client = openai.Client(
        api_key=OPENAI_API_KEY,
    )
    response = client.embeddings.create(
        input=summary,
        model=model
    )
    return response.data[0].embedding


def do_create_dandiset_summaries():
    dandisets = fetch_all_dandisets()
    for dandiset_index, dandiset in enumerate(dandisets):
        dandiset_id = dandiset.dandiset_id
        dandiset_version = dandiset.version
        dandiset_dir = f"{parent_dir}/dandisets/{dandiset_id}"
        if os.path.exists(f"{dandiset_dir}/summary.md"):
            print(f"Summary already exists for {dandiset_id}.")
            continue
        print(f"Creating summary for {dandiset_id} ({dandiset_index + 1}/{len(dandisets)})...")
        try:
            dandiset_summarizer(
                dandiset_id=dandiset_id,
                dandiset_version=dandiset_version,
                cache_dir=f"{parent_dir}/cache",
                # gpt_model="gpt-4o-mini"
                gpt_model="gpt-4o"
            )
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"Failed to create summary for {dandiset_id}: {e}")
            with open(f"{dandiset_dir}_error.txt", "w") as f:
                f.write(str(e))


class Dandiset(BaseModel):
    dandiset_id: str
    version: str


def fetch_all_dandisets():
    url = "https://api.dandiarchive.org/api/dandisets/?page=1&page_size=5000&ordering=-modified&draft=true&empty=false&embargoed=false"
    with urllib.request.urlopen(url) as response:
        X = json.loads(response.read())

    dandisets: List[Dandiset] = []
    for ds in X["results"]:
        pv = ds["most_recent_published_version"]
        dv = ds["draft_version"]
        dandisets.append(
            Dandiset(
                dandiset_id=ds["identifier"],
                version=pv["version"] if pv else dv["version"],
            )
        )

    return dandisets


@click.command()
@click.option("--dandiset-id", required=True)
@click.option("--dandiset-version", required=True)
@click.option("--cache-dir", required=True)
def create_dandiset_summary(dandiset_id: str, dandiset_version: str, cache_dir: str):
    dandiset_summarizer(
        dandiset_id=dandiset_id, dandiset_version=dandiset_version, cache_dir=cache_dir,
        gpt_model="gpt-4o-mini"
    )


@click.command()
def create_dandiset_summaries():
    do_create_dandiset_summaries()


@click.command()
def create_embeddings():
    do_create_embeddings()


@click.group()
def cli():
    pass


cli.add_command(create_dandiset_summaries)
cli.add_command(create_dandiset_summary)
cli.add_command(create_embeddings)

if __name__ == "__main__":
    cli()
