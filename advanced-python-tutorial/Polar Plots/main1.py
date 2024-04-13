# pip install matplotlib, numpy

import math
import matplotlib.pyplot as plt

x = 20
y = 30

plt.scatter(x, y)
plt.xlim(0, 40)
plt.ylim(0, 40)
plt.grid()
plt.show()

r = math.sqrt(x**2 + y**2)
theta = math.atan(y / x)

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
plt.scatter(theta, r)
plt.show()
