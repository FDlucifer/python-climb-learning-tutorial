# pip install bokeh numpy

import numpy as np
from bokeh.plotting import figure, show, curdoc

curdoc().theme = "dark_minimal"

x = np.random.random(50) * 10
y = np.random.random(50) * 200

p = figure(title="simple scatter plot", x_axis_label="x", y_axis_label="y")
p.width = 1280
p.height = 720

circle = p.circle(x, y, legend_label="random points", color="yellow", size=12)

glyph = circle.glyph
glyph.size = 20
glyph.fill_color = "red"

show(p)