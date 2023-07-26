# pip install scikit-learn numpy

import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = load_breast_cancer()
x, y = data.data, data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

tree_list = []
for i in range(100):
    tree = DecisionTreeClassifier(max_features="sqrt")
    subset_indices = np.random.choice(np.arange(len(x_train)), size=len(x_train) // 2)
    x_train_subset = x_train[subset_indices]
    y_train_subset = y_train[subset_indices]
    tree.fit(x_train_subset, y_train_subset)
    tree_list.append(tree)

preds = []
for i, tree in enumerate(tree_list):
    individual_preds = tree.predict(x_test)
    individual_accuracy = accuracy_score(y_test, individual_preds)
    print(f"tree {i + 1} accuracy: {individual_accuracy}")
    preds.append(individual_preds)

preds = np.array(preds)
ensemble_predictions = np.round(np.mean(preds, axis=0))

ensemble_accuracy = accuracy_score(y_test, ensemble_predictions)
print(ensemble_accuracy)

rf = RandomForestClassifier(n_estimators=100)
rf.fit(x_train, y_train)
rf_preds = rf.predict(x_test)

print(accuracy_score(y_test, rf_preds))
