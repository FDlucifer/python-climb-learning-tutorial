import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import cross_val_score, GridSearchCV

mnist = fetch_openml("mnist_784", version=1)
print(mnist.keys())

x, y = mnist['data'], mnist['target']
x = x.to_numpy()
y = y.to_numpy()

x_train, x_test, y_train, y_test = x[:60000], x[60000:], y[:60000], y[60000:]

from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=1, weights="uniform")
print(clf.fit(x_train, y_train))
print(clf.score(x_test, y_test))
print(cross_val_score(clf, x_train, y_train, cv=3, scoring="accuracy"))

param_grid = [{
    "n_neighbors": [1,3,5,7], "weights": ["uniform", "distance"]
}]
grid_search = GridSearchCV(clf, param_grid, cv=3, scoring="accuracy", return_train_score=True, verbose=10)
print(grid_search.fit(x_train, y_train))

final_clf = grid_search.best_estimator_
print(final_clf.score(x_test, y_test))