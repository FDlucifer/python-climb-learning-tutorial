import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x = np.arange(0,30,0.2)
y1 = np.sin(x)
y2 = np.cos(x)

plt.title("sine function")
plt.xlabel("weight of students")
plt.xlabel("height of students")

plt.plot(x,y1)
plt.plot(x,y2)
plt.show()