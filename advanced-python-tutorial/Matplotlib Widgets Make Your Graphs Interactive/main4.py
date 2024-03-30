import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

t = np.linspace(0.0, 2 * np.pi, 1000)
a, b = 1.0, 1.0
x = a * np.sin(t)
y = b * np.cos(t)
(l,) = ax.plot(x, y)

ax_slider_a = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor="lightgoldenrodyellow")
ax_slider_b = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor="lightgoldenrodyellow")
slider_a = Slider(ax_slider_a, "a", 0.1, 5.0, valinit=a)
slider_b = Slider(ax_slider_b, "b", 0.1, 5.0, valinit=b)


def update(val):
    a = slider_a.val
    b = slider_b.val
    l.set_xdata(a * np.sin(t))
    l.set_xdata(b * np.cos(t))
    fig.canvas.draw_idle()


slider_a.on_changed(update)
slider_b.on_changed(update)

plt.show()
