# https://github.com/ollama/ollama

import faiss
import requests
import numpy as np

res = requests.post(
    "http://localhost:11434/api/embeddings",
    json={"model": "llama2", "prompt": "hello world"},
)

print(len(res.json()["embedding"]))

d = 4096

titles = []

index = faiss.IndexFlatL2(d)

X = np.zeros((len(titles), d), dtype="float32")

for i, title in enumerate(titles):
    res = requests.post(
        "http://localhost:11434/api/embeddings",
        json={"model": "llama2", "prompt": title},
    )

    embedding = res.json()["embedding"]
    X[i] = np.array(embedding)

index.add(X)
