# pip install plotext numpy
import plotext
import numpy as np

x = np.random.random(100)
y = np.random.random(100)

plotext.scatter(x, y)
plotext.title("random data points")
plotext.show()


x = np.arange(0,10,0.1)
y = np.sin(x)
y2 = np.cos(x)

plotext.plot(x, y, label="sin")
plotext.plot(x, y2, label="cos")
plotext.title("SIN & cos")
plotext.show()