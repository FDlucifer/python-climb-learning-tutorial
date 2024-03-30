import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

x = np.linspace(0, 10, 1000)
y = np.sin(x)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

(line,) = ax.plot(x, y, lw=2)

axcolor = "lightgoldenrodyellow"
ax_zoom_in = plt.axes([0.7, 0.05, 0.1, 0.075], facecolor=axcolor)
ax_zoom_out = plt.axes([0.81, 0.05, 0.1, 0.075], facecolor=axcolor)

button_zoom_in = Button(ax_zoom_in, "zoom in")
button_zoom_out = Button(ax_zoom_out, "zoom out")


def zoom_in(event):
    xlims = ax.get_xlim()
    new_xlims = [xlims[0] * 1.1, xlims[1] * 0.9]
    ax.set_xlim(new_xlims)
    plt.draw()


def zoom_out(event):
    xlims = ax.get_xlim()
    new_xlims = [xlims[0] * 0.9, xlims[1] * 1.1]
    ax.set_xlim(new_xlims)
    plt.draw()


button_zoom_in.on_clicked(zoom_in)
button_zoom_out.on_clicked(zoom_out)


plt.show()
