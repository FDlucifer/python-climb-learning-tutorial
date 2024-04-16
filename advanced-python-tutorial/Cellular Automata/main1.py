# pip install cellpylib numpy matplotlib

import numpy as np
import cellpylib as cpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

cellular_automation = cpl.init_simple2d(60, 60)
cellular_automation[:, [28, 29, 30, 30], [30, 31, 29, 31]] = 1
cellular_automation[:, [40, 40, 40], [15, 16, 17]] = 1
cellular_automation[
    :, [18, 18, 19, 20, 21, 21, 21, 21, 20], [45, 48, 44, 44, 44, 45, 46, 47, 48]
] = 1

cellular_automation = cpl.evolve2d(
    cellular_automation,
    timesteps=250,
    neighbourhood="Moore",
    apply_rule=cpl.game_of_life_rule,
    memoize="recursive",
)

# cpl.plot2d(cellular_automation)

fig, ax = plt.subplots()
ax.set_xlim((0, 60))
ax.set_ylim((0, 60))

img = ax.imshow(cellular_automation[0], interpolation="nearest", cmap="Greys")


def init():
    img.set_data(cellular_automation[0])
    return (img,)


def animate(i):
    img.set_data(cellular_automation[i])
    return (img,)


ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=250, interval=30, blit=True, repeat=False
)
plt.show()
