import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from skimage import data, exposure


image = data.moon()

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)
img_ax = ax.imshow(image, cmap="gray")

ax_slider = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor="lightgoldenrodyellow")
slider = Slider(ax_slider, "Brightness", 0.5, 2.0, valinit=1.0)


def update(val):
    brightness = slider.val
    updated_image = exposure.adjust_gamma(image, gamma=1, gain=brightness)
    img_ax.set_data(updated_image)
    fig.canvas.draw_idle()


slider.on_changed(update)
plt.show()
