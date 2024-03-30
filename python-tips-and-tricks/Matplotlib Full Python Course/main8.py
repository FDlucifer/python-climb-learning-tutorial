# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("dark_background")

votes = [10, 2, 5, 16, 22]
people = ["A", "B", "C", "D", "E"]

plt.pie(votes, labels=None)
plt.legend(labels=people)

plt.show()
