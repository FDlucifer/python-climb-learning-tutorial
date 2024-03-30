from datetime import date
from operator import mod
from sys import modules
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits

digits = load_digits()
data = scale(digits.data)

model = KMeans(n_clusters=10, init='random', n_init=10)
model.fit(data)

model.predict([...])