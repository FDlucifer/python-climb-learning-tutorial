import numpy as np
import matplotlib.pyplot as plt

#x = np.linspace(-100,100,201)
x = np.arange(-100,101,1)
y = 0.5 * x ** 2 + 2 * x

plt.plot(x, y,'y^')
plt.show()