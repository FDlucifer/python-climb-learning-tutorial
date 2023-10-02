# pip install pandas matplotlib scikit-learn

import pandas as pd

df = pd.read_csv("income.csv")

df = pd.concat(
    [
        df.drop("workclass", axis=1),
        pd.get_dummies(df["workclass"]).add_prefix("workclass_"),
    ],
    axis=1,
)
df = pd.concat(
    [
        df.drop("education", axis=1),
        pd.get_dummies(df["education"]).add_prefix("education_"),
    ],
    axis=1,
)
df = pd.concat(
    [
        df.drop("marital-status", axis=1),
        pd.get_dummies(df["marital-status"]).add_prefix("marital-status_"),
    ],
    axis=1,
)
df = pd.concat(
    [
        df.drop("occupation", axis=1),
        pd.get_dummies(df["occupation"]).add_prefix("occupation_"),
    ],
    axis=1,
)
df = pd.concat(
    [
        df.drop("relationship", axis=1),
        pd.get_dummies(df["relationship"]).add_prefix("relationship_"),
    ],
    axis=1,
)
df = pd.concat(
    [df.drop("race", axis=1), pd.get_dummies(df["race"]).add_prefix("race_")], axis=1
)
df = pd.concat(
    [
        df.drop("native-country", axis=1),
        pd.get_dummies(df["native-country"]).add_prefix("native-country_"),
    ],
    axis=1,
)

df["gender"] = df["gender"].apply(lambda x: 1 if x == "Male" else 0)
df["income"] = df["income"].apply(lambda x: 1 if x == ">50K" else 0)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt

x = df.drop("income", axis=1)
y = df["income"]

forest = RandomForestClassifier(n_jobs=-1, random_state=42)
forest.fit(x, y)

f1_score = []
features = []

num_features_start = x.shape[1]

while x.shape[1] > 0:
    print(f"training rf on the {x.shape[1]} most important features.")
    feature_importances = forest.feature_importances_

    y_pred = forest.predict(x)
    f1 = f1_score(y, y_pred)
    f1_score.append(f1)
    features.append(x.columns)

    if x.shape[1] == 1:
        break

    least_important_idx = feature_importances.argmin()
    x = x.drop(x.columns[least_important_idx], axis=1)
    forest.fit(x, y)

num_features = range(num_features_start, 0, -1)
plt.plot(num_features, f1_score)
plt.xlabel('number of features')
plt.ylabel('f1 scores')
plt.title('number of features vs f1 score')
plt.xlim(num_features_start+5, 1-5)
plt.show()

