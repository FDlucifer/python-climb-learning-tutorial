# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

ax = plt.axes(projection="3d")

x = np.arange(0, 50, 0.1)
y = np.sin(x)
z = np.cos(x)

ax.scatter(x, y, z)
ax.set_title("3D Plot")
ax.set_xlabel("test")
plt.show()
