import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

amp = 1.0
freq = 1.0

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

t = np.linspace(0.0, 2 * np.pi, 1000)
s = amp * np.sin(freq * t)
(l,) = ax.plot(t, s, lw=2)

ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor="lightgoldenrodyellow")
slider = Slider(ax_slider, "Frequency", 0.1, 5.0, valinit=freq)


def update(val):
    freq = slider.val
    l.set_ydata(amp * np.sin(freq * t))
    fig.canvas.draw_idle()


slider.on_changed(update)

plt.show()
