# pip install scikit-learn matplotlib lime

import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from lime import lime_tabular

data = load_breast_cancer()
x, y = data["data"], data["target"]

print(x)
print(y)
print(data["target_names"])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

forest_clf = RandomForestClassifier()
forest_clf.fit(x_train, y_train)

print(forest_clf.score(x_test, y_test))

explainer = lime_tabular.LimeTabularExplainer(
    training_data=x_train,
    feature_names=data['feature_names'],
    class_names=data['target_names'],
    mode='classification'
)

for i in range(20):
    print('correct: ', 'begin' if y_test[i] else 'malignant')
    print('classification: ', forest_clf.predict([x_test[i]]))
    print(dict(zip(data['feature_names'], x_test[i])))

    explanation = explainer.explain_instance(
        data_row=x_test[i],
        predict_fn=forest_clf.predict_proba,
        num_features=30
    )

    fig = explanation.as_pyplot_figure()
    plt.tight_layout()
    plt.show()
