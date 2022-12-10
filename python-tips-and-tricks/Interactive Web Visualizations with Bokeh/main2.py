# pip install bokeh numpy

import numpy as np
from bokeh.plotting import figure, show

x = np.arange(0,5,1)
y = np.random.random(5) * 100

p = figure(title="simple bar plot", x_axis_label="x", y_axis_label="y")

p.vbar(x=x, top=y, width=0.5, bottom=0, color="red")

show(p)