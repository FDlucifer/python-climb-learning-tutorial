# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x = np.arange(100)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("sine wave")

axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title("cosine wave")

axs[1, 0].plot(x, np.random.random(100))
axs[1, 0].set_title("random function")

axs[1, 1].plot(x, np.log(x))
axs[1, 1].set_title("log function")
axs[1, 1].set_xlabel("TEST")

fig.suptitle("four plots")
plt.tight_layout()
plt.savefig("fourplots.png", dpi=300, transparant=False, bbox_inches="tight")
plt.show()
