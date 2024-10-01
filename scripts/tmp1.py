import json
import numpy as np
import openai
import os


def main():
    with open('embeddings.json', 'r') as f:
        embeddings = json.load(f)
    model_name = 'text-embedding-3-large'
    embeddings_list = []
    dandiset_ids = []
    for dandiset_id, embeddings in embeddings.items():
        embedding = embeddings[model_name]
        embeddings_list.append(np.array(embedding))
        dandiset_ids.append(dandiset_id)
    embeddings_array = np.array(embeddings_list)
    print(embeddings_array.shape)

    # tsne
    from sklearn.manifold import TSNE
    import matplotlib.pyplot as plt

    tsne = TSNE(n_components=3, random_state=0, perplexity=30)
    embeddings_tsne = tsne.fit_transform(embeddings_array)

    plt.figure(figsize=(6, 6))
    plt.scatter(embeddings_tsne[:, 0], embeddings_tsne[:, 1])
    # for i, dandiset_id in enumerate(dandiset_ids):
    #     plt.annotate(dandiset_id, (embeddings_tsne[i, 0], embeddings_tsne[i, 1]))
    plt.show()

    prompt = 'neural units for mouse licking behavior'
    prompt_embedding = _compute_embedding(prompt, model=model_name)

    # cosine similarity
    from sklearn.metrics.pairwise import cosine_similarity
    similarities = cosine_similarity(prompt_embedding.reshape(1, -1), embeddings_array)
    # order by similarity
    order = np.argsort(similarities[0])[::-1]
    for i in order:
        print(dandiset_ids[i], similarities[0, i])


def _compute_embedding(prompt: str, *, model: str):
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise Exception("OPENAI_API_KEY environment variable not set.")
    client = openai.Client(
        api_key=OPENAI_API_KEY,
    )
    response = client.embeddings.create(
        input=prompt,
        model=model
    )
    return np.array(response.data[0].embedding)


if __name__ == '__main__':
    main()
