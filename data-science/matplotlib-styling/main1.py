import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from numpy.core.numerictypes import LOWER_TABLE

x = np.arange(0,30,0.2)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label="sine")
plt.plot(x,y2,label="cosine")
plt.legend(loc="lower right")

plt.show()