import matplotlib.pyplot as plt
import random

dice_sums = [0] * 12

for x in range(10000):
    dice_sum = random.randint(1, 6) + random.randint(1, 6)
    dice_sums[dice_sum - 1] += 1
    if x % 200 == 0:
        plt.bar([1,2,3,4,5,6,7,8,9,10,11,12], dice_sums, color=("blue"))
        plt.pause(0.001)

plt.show()