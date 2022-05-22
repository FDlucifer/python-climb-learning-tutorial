# pip install numpy matplotlib

import numpy as np
import matplotlib.pyplot as plt

labels = ["Chrome", "Firefox", "Safari"]
shares = np.array([
    [0.5,0.3,0.2],
    [0.4,0.4,0.1],
    [0.4,0.4,0.1],
    [0.3,0.2,0.5],
    [0.4,0.3,0.3],
    [0.3,0.3,0.4],
    [0.4,0.2,0.4],
    [0.5,0.4,0.1]
])

years = [2010 + i for i in range(8)]

plot_steps = np.array([shares[0]])
last_shares = shares[0]
for i in range(1, len(shares)):
    difference = shares[i] - last_shares
    difference /= 100
    for j in range(101):
        plot_steps = np.append(plot_steps, [last_shares + difference * j], 0)
    last_shares = shares[i]

print(plot_steps)

years = iter(years)
year = next(years)

for i, step in enumerate(plot_steps):
    if i % 100 == 0:
        year = next(years)
    plt.xlim(0,1)
    plt.barh(labels, step, color=["green","orange","cyan"])
    plt.text(0.8, 0.2, year, fontsize=14)
    plt.pause(0.01)
    plt.clf()

plt.show()