# pip install -U scikit-learn

from operator import mod
from statistics import mode
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5,15,25,35,45,55]).reshape((-1,1))
y = np.array([5,20,14,32,22,38])

print(x.shape)
print(y.shape)

model = LinearRegression()
print(model.fit(x,y))
print(model.intercept_)
print(model.coef_)

r_sq = model.score(x,y)
print(r_sq)

y_pred = model.predict(x)
print(y_pred)

y = model.intercept_ + model.coef_ * x
print(y)

x_new = np.arange(5).reshape((-1,1))
print(x_new)

y_new = model.predict(x_new)
print(y_new)