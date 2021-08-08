from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

data = load_breast_cancer()

print(data.feature_names)
print(data.target_names)

x_train, x_test, y_train, y_test = train_test_split(np.array(data.data),np.array(data.target), test_size=0.2)

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(x_train, y_train)

print(clf.score(x_test, y_test))