import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
from skimage import data


img = data.camera()
fig, ax = plt.subplots()
ax.imshow(img, cmap="gray")

coords = [0, img.shape[1], img.shape[0], 0]


def toggle_selector(event):
    if event.key == "r":
        ax.set_xlim(0, img.shape[1])
        ax.set_ylim(img.shape[0], 0)
        fig.canvas.draw_idle()


def line_select_callback(eclick, erelease):
    coords[0], coords[1] = eclick.xdata, erelease.xdata
    coords[2], coords[3] = erelease.ydata, eclick.ydata
    ax.set_xlim(coords[0], coords[1])
    ax.set_ylim(coords[2], coords[3])
    fig.canvas.draw_idle()


rs = RectangleSelector(
    ax,
    line_select_callback,
    drawtype="box",
    useblit=True,
    button=[1, 3],
    minspanx=5,
    minspany=5,
    spancoords="pixels",
    interactive=True,
)

fig.canvas.mpl_connect("key_press_event", toggle_selector)
plt.show()
