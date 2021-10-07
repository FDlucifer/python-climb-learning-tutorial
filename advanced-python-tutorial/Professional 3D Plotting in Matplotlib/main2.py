# pip install matplotlib numpy

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# single points
ax = plt.axes(projection="3d")

x_data = np.arange(0, 50, (0.1))
y_data = np.arange(0, 50, (0.1))
z_data = np.sin(x_data) * np.cos(y_data)

ax.plot(x_data, y_data, z_data)
ax.set_title("funny function")
ax.set_xlabel("my x values (cm)")
ax.set_ylabel("my y values (v)")
ax.set_zorder("my fancy results (cm*v)")
plt.show()