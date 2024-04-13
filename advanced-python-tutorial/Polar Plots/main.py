# pip install matplotlib

import math
import matplotlib.pyplot as plt

r = 20
theta = math.pi / 2

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
ax.scatter(theta, r)

plt.show()
