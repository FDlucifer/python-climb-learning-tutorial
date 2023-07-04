# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

x = ["c++", "c#", "python", "java", "go"]
y = [20, 50, 140, 1, 45]

plt.bar(x, y, color="r", align="edge", width=0.5, edgecolor="green", lw=6)
plt.show()
