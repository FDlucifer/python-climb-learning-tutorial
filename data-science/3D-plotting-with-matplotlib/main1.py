import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection="3d")

def z_function(x,y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-50,50,100)
y = np.linspace(-50,50,100)

X, Y = np.meshgrid(x,y)
Z = z_function(X, Y)

ax.plot_surface(X,Y,Z)

plt.show()