# pip install txtai numpy pandas streamlit

import txtai
import numpy as np
import pandas as pd

np.random.seed(1)

df = pd.read_csv("seth-data.csv").dropna()
content = df.content_plain.values
# titles = df.dropna().sample(100000).TITLE.values

embeddings = txtai.Embeddings({"path": "sentence-transformers/all-MiniLM-L6-v2"})

embeddings.index(content)
embeddings.save("embeddings_seth.tar.gz")
# embeddings.load('embeddings.tar.gz')

# result = embeddings.search("protector for cam", 5)

# print(result)

# actual_results = [titles[x[0]] for x in result]

# print(actual_results)
