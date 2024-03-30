# pip install numpy matplotlib sklearn scikit-learn

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = 4 * np.random.rand(100, 1) - 2
Y = 4 + 2 * X + 5 * X**2 + 10 * np.random.randn(100, 1)

poly_features = PolynomialFeatures(degree=6, include_bias=False)
X_poly = poly_features.fit_transform(X)

reg = LinearRegression()
reg.fit(X_poly, Y)

X_vals = np.linspace(-2, 2, 100).reshape(-1, 1)
X_vals_poly = poly_features.transform(X_vals)

Y_vals = reg.predict(X_vals_poly)

plt.scatter(X, Y)
plt.plot(X_vals, Y_vals, color="r")
plt.show()