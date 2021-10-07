# pip install matplotlib numpy

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# single points
ax = plt.axes(projection="3d")
ax.scatter(3,5,7)
plt.show()