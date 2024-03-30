# pip install numpy pandas matplotlib scikit-learn seaborn

import random
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = load_breast_cancer()

X = data['data']
Y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))
print(data['feature_names'])

X_new = np.array(random.sample(range(0,50), 30))
print(data['target_names'][clf.predict([X_new])[0]])

column_data = np.concatenate([data['data'], data['target'][:, None]], axis=1)
column_names = np.concatenate([data['feature_names'], ["class"]])
df = pd.DataFrame(column_data, columns=column_names)

print(df.corr())
sns.heatmap(df.corr(), cmap="coolwarm", annot=True, annot_kws={"fontsize": 8})
plt.tight_layout()
plt.show()