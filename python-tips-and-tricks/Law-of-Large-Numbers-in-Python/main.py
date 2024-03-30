import matplotlib.pyplot as plt
import random

heads_tails = [0, 0]

for x in range(10000):
    heads_tails[random.randint(0, 1)] += 1
    if x % 50 == 0:
        plt.bar([0,1], heads_tails, color=("blue", "red"))
        plt.pause(0.01)

plt.show()