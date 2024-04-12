# pip install scikit-learn matplotlib lime

import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
x, y = data["data"], data["target"]

print(x)
print(y)
print(data["target_names"])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

tree_clf = DecisionTreeClassifier()
tree_clf.fit(x_train, y_train)

print(tree_clf.score(x_test, y_test))

plt.figure(figsize=(20, 10))
plot_tree(
    tree_clf,
    filled=True,
    feature_names=data["feature_names"],
    class_names=data["target_names"],
    rounded=True,
)
plt.show()


