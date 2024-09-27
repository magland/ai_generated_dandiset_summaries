#!/usr/bin/env python

from typing import List
import os
import json
import time
import click
import dandi.dandiarchive as da
import lindi


def dandiset_summarizer(*, dandiset_id: str, dandiset_version: str, cache_dir: str):
    dandiset_raw_metadata = _get_raw_metadata_for_dandiset(dandiset_id=dandiset_id)

    asset_objects = _get_asset_objects_for_dandiset(
        dandiset_id=dandiset_id, cache_dir=cache_dir
    )

    neurodata_summaries = []
    for asset in asset_objects:
        lindi_fname = _get_local_lindi_file(
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
        raise Exception(
            f"Found {len(clusters)} clusters. This is too many to summarize."
        )

    representative_lindi_fnames = [
        _get_local_lindi_file(
            asset_id=asset_objects[cluster[0]]["identifier"],
            asset_path=asset_objects[cluster[0]]["path"],
            url=asset_objects[cluster[0]]["download_url"],
            cache_dir=cache_dir,
        )
        for cluster in clusters
    ]
    txt = _create_cluster_summary_text(
        dandiset_id=dandiset_id,
        representative_lindi_fnames=representative_lindi_fnames,
        cluster_sizes=[len(cluster) for cluster in clusters],
        dandiset_raw_metadata=dandiset_raw_metadata,
    )
    print(txt)


def _create_cluster_summary_text(
    *,
    dandiset_id: str,
    representative_lindi_fnames: List[str],
    cluster_sizes: List[int],
    dandiset_raw_metadata: dict,
):
    total_num_nwb_files = sum(cluster_sizes)
    txt_lines = []

    txt_lines.append('''
Below is an auto-generated summary of the contents of a Dandiset.
Please summarize the experiments and provide information on what data are available.
You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.
Provide details that would be useful to someone who wants to reuse and reanalyze the dataset.
The summaries are from representative NWB files for each type, so keep that in mind when making your description.
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


def _get_asset_objects_for_dandiset(dandiset_id: str, cache_dir: str):
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
    parsed_url = da.parse_dandi_url(f"https://dandiarchive.org/dandiset/{dandiset_id}")
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


def _get_local_lindi_file(*, asset_id: str, asset_path: str, url: str, cache_dir: str):
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    if not os.path.exists(f"{cache_dir}/assets"):
        os.makedirs(f"{cache_dir}/assets")
    lindi_fname = f"{cache_dir}/assets/{asset_id}.lindi.json"
    if not os.path.exists(lindi_fname):
        print(f"Creating {lindi_fname} for {asset_path}...")
        with lindi.LindiH5pyFile.from_hdf5_file(url) as lindi_file:
            lindi_file.write_lindi_file(lindi_fname)
    return lindi_fname


@click.command()
@click.option("--dandiset-id", required=True)
@click.option("--dandiset-version", required=True)
@click.option("--cache-dir", required=True)
def main(dandiset_id: str, dandiset_version: str, cache_dir: str):
    dandiset_summarizer(
        dandiset_id=dandiset_id, dandiset_version=dandiset_version, cache_dir=cache_dir
    )


if __name__ == "__main__":
    main()
