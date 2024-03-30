# pip install bokeh numpy

import numpy as np
from bokeh.layouts import row
from bokeh.plotting import figure, show, curdoc

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

p1 = figure()
p1.line(x, y1)

p2 = figure()
p2.line(x, y2)

p3 = figure()
p3.line(x, y3)

show(row(children=[p1,p2,p3], sizing_mode="scale_width"))

