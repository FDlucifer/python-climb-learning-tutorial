import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

x = np.random.rand(10)
y = np.random.rand(10)
fig, ax = plt.subplots()
(points,) = plt.plot(x, y, "o", picker=5)

annotations = []


def on_pick(event):
    ind = event.ind[0]
    annot = ax.annotate(
        f"({x[ind]:.2f}, {y[ind]:.2f})",
        (x[ind], y[ind]),
        xytext=(15, -15),
        textcoords="offset points",
        arrowprops=dict(arrowstyle="->"),
    )
    annotations.append(annot)
    fig.canvas.draw_idle()


def clear_annotations(event):
    for annot in annotations:
        annot.remove()
    annotations.clear()
    fig.canvas.draw_idle()


ax_button = plt.axes([0.7, 0.01, 0.2, 0.075])
btn = Button(ax_button, "clear annotations")
btn.on_clicked(clear_annotations)

fig.canvas.mpl_connect("pick_event", on_pick)
plt.show()
