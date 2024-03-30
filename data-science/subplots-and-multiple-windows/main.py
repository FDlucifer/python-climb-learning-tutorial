import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100,0.2)
y1 = np.sin(x)
y2 = x ** 2 + 2 * x

ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

ax1.plot(x,y1)
ax2.plot(x,y2)
ax3.plot(x,y1,'r')
ax4.plot(x,y2,'g')

plt.tight_layout()
plt.show()