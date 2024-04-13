# pip install scikit-learn

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
x, y = data["data"], data["target"]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2)
x_train_train, x_calib, y_train_train, y_calib = train_test_split(
    x_train, y_train, test_size=0.2
)

clf = LinearSVC()
clf.fit(x_train_train, y_train_train)

calib_clf = CalibratedClassifierCV(clf, cv=3)
calib_clf.fit(x_calib, y_calib)

print(clf.score(x_test, y_test))
print(calib_clf.score(x_test, y_test))

print(clf.predict([x_test[5]]))
print(calib_clf.predict_proba([x_test[5]]))
