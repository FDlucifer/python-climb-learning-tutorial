# pip install bokeh numpy

import numpy as np
from bokeh.plotting import figure, show

x = np.arange(0, 10, 1)
y1 = x ** 2
y2 = x ** 3
y3 = x ** 4

p = figure(title="simple line charts", x_axis_label="x", y_axis_label="y")

p.line(x, y1, legend="quadratic function", line_width=2, color="red")
p.line(x, y2, legend="cubic function", line_width=2, color="green")
p.line(x, y3, legend="quartic function", line_width=2, color="blue")

show(p)