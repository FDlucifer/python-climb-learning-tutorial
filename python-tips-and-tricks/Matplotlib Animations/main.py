# pip install matplotlib
# pip install scikit-learn
# pip install numpy
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import random

reg = LinearRegression()

x_values = []
y_values = []

for i in range(1000):
    plt.clf()
    x_values.append(random.randint(0,100))
    y_values.append(random.randint(0,100))

    x = np.array(x_values)
    x = x.reshape(-1, 1)

    y = np.array(y_values)
    y = y.reshape(-1, 1)

    if i % 5 == 0:
        reg.fit(x, y)
        plt.xlim(0,100)
        plt.ylim(0,100)
        plt.scatter(x_values, y_values, color='black')
        plt.plot(list(range(100)), reg.predict(np.array([x for x in range(100)]).reshape(-1,1)))
        plt.pause(0.001)

plt.show()