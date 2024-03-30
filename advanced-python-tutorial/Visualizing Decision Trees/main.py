# pip install scikit-learn matplotlib

from sklearn.datasets import load_iris
data = load_iris()
x, y = data.data, data.target

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(x,y)

from sklearn import tree

print(tree.export_text(clf))

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(50,30))
print(tree.plot_tree(clf, feature_names=data.feature_names, class_names=data.target_names, filled=True))

tree.export_graphviz(clf, out_file=open("tree.dot", "w"), feature_names=data.feature_names)
# https://onlineconvertfree.com/convert/

