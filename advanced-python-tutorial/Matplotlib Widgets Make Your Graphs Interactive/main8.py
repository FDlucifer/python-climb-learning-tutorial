import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
ax.plot(x, y, label="sin(x)")

initial_x = 5
initial_y = 0.5

vline = ax.axvline(initial_x, color="r", linestyle="--")
hline = ax.axvline(initial_y, color="b", linestyle="--")

ax_slider_x = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor="lightgoldenrodyellow")
ax_slider_y = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor="lightgoldenrodyellow")

slider_x = Slider(ax_slider_x, "X", 0, 10, valinit=initial_x)
slider_y = Slider(ax_slider_y, "Y", -1, 1, valinit=initial_y)


def update_x(val):
    vline.set_xdata(slider_x.val)
    fig.canvas.draw_idle()


def update_y(val):
    hline.set_ydata(slider_y.val)
    fig.canvas.draw_idle()


slider_x.on_changed(update_x)
slider_y.on_changed(update_y)

plt.show()
