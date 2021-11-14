# pip install matplotlib numpy
# bubble sort

import matplotlib.pyplot as plt
import numpy as np

amount = 15

lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

n = len(lst)
for i in range(n):
    for j in range(0, n-i-1):
        plt.bar(x, lst)
        plt.pause(0.001)
        plt.clf()
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
plt.show()