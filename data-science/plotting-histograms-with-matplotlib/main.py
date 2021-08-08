import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 172, 8
x = mu + sigma * np.random.random(10000)

plt.hist(x, 100, facecolor='blue', density=True)
plt.xlabel('heights')
plt.ylabel('percentage of students')
plt.title("heights of students")
plt.text(145,0.04,"u = 172, sig = 8")
plt.grid(True)
plt.show()