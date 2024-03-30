import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

x = np.random.random(200)
y = np.random.random(200)
classes = np.random.randint(0, 3, 200)

custom_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("custom", ["red", "blue", "yellow", "green"])

plt.scatter(x,y,c=classes,cmap=custom_cmap)
plt.colorbar()
plt.show()