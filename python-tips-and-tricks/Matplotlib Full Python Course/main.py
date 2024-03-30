# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

X_data = np.random.random(1000) * 100
Y_data = np.random.random(1000) * 100

plt.scatter(X_data, Y_data, c="red", s=150, marker="*", alpha=0.3)
plt.show()
