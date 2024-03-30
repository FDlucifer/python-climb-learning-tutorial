# streamlit run main_streamlit.py

import streamlit as st
import numpy as np
import pandas as pd
import txtai


def load_data_and_embeddings():
    # np.random.seed(1)
    df = pd.read_csv("seth-data.csv").dropna()
    titles = df.title.values
    urls = df.url.values
    # titles = df.dropna().sample(100000).TITLE.values

    embeddings = txtai.Embeddings({"path": "sentence-transformers/all-MiniLM-L6-v2"})

    embeddings.load("embeddings_seth.tar.gz")

    return titles, urls, embeddings


titles, urls, embeddings = st.cache_data(load_data_and_embeddings)()
# st.title("Amazon Item Search Engine")
st.title("seth blog post Search Engine")
query = st.text_input("enter a search query:", "")

if st.button("Search"):
    if query:
        result = embeddings.search(query, 5)
        actual_results = [f'title: {titles[x[0]]}, url: {urls[x[0]]}' for x in result]
        for res in actual_results:
            st.write(res)
    else:
        st.write("Please enter a query")

