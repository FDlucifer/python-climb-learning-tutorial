# pip install cellpylib numpy matplotlib

import numpy as np
import cellpylib as cpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

cellular_automation = cpl.init_simple2d(60, 60)

cellular_automation = cpl.evolve2d(
    cellular_automation,
    timesteps=30,
    neighbourhood="Moore",
    apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=126),
)

cpl.plot2d_animate(cellular_automation)
