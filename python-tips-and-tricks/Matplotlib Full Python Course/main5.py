# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

heights = np.random.normal(172, 8, 300)

plt.boxplot(heights)
plt.show()
