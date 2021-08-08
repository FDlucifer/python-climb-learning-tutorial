import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection="3d")

z = np.linspace(0, 30, 100)
x = np.sin(z)
y = np.cos(z)

ax.plot3D(x,y,z)

plt.show()