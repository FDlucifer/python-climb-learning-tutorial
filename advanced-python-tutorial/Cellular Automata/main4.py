# pip install cellpylib numpy matplotlib

import numpy as np
import cellpylib as cpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class CutomRule(cpl.BaseRule):
    def __call__(self, n, c, t):
        # return n[1] + 1
        # return 1 if n[0] != n[2] else 0
        # return n[1] + 1 if n[0] != n[2] else n[1] - 1
        if n[1][1] == 0:
            if np.sum(n) == 3:
                return 1
            else:
                return 0
        else:
            if np.sum(n) - 1 == 2 or np.sum(n) - 1 == 3 or np.sum(n) - 1 == 4:
                return 1
            else:
                return 0


rule = CutomRule()
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
    apply_rule=rule,
    memoize="recursive",
)


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
    fig, animate, init_func=init, frames=250, interval=50, blit=True, repeat=False
)
plt.show()

