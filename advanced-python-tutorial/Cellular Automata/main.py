# pip install cellpylib numpy matplotlib

import numpy as np
import cellpylib as cpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

cellular_automation = np.array([[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]])
cellular_automation = cpl.init_simple(100)

cellular_automation = cpl.evolve(
    cellular_automation,
    timesteps=50,
    memoize=True,
    apply_rule=lambda n, c, t: cpl.nks_rule(n, 110),
)

cpl.plot(cellular_automation)

fig, ax = plt.subplots()
mat = ax.matshow(cellular_automation, cmap="binary")
plt.axis("off")


def animate(i):
    mat.set_data(cellular_automation[: i + 1])
    return [mat]


ani = animation.FuncAnimation(
    fig, animate, frames=50, interval=50, blit=True, repeat=False
)
plt.show()
