# pip install plotext numpy

import plotext
import numpy as np

l = 1000
x = range(1, l+1)
frames = 50

plotext.title("sine animation")
plotext.clc()

for i in range(frames):
    plotext.clt()
    plotext.cld()

    y = plotext.sin(1, 4, l, 2 * i / frames)
    plotext.xlim(0, 400)
    plotext.plot(x, y, marker="dot", color="red")
    plotext.sleep(0.01)
    plotext.show()

