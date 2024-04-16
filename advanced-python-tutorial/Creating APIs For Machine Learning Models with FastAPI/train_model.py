import pickle
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

x, y = fetch_openml("mnist_784", version=1, return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

clf = RandomForestClassifier(n_jobs=-1)

clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))
with open("mnist_model.pkl", "wb") as f:
    pickle.dump(clf, f)
