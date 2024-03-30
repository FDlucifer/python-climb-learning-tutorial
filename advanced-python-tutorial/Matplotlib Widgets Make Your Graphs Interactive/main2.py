import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
(l,) = ax.plot(x, y)

axcolor = "lightgoldenrodyellow"
ax_radio = plt.axes([0.05, 0.4, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(ax_radio, ("line", "scatter", "bar"))


def plot_type(label):
    ax.clear()
    if label == "line":
        ax.plot(x, y)
    elif label == "scatter":
        ax.scatter(x, y)
    elif label == "bar":
        ax.bar(x, y, width=0.1)
    fig.canvas.draw_idle()


radio.on_clicked(plot_type)

plt.show()
