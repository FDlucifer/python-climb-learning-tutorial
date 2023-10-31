import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)

(l1,) = ax.plot(x, np.sin(x), visible=False, label="sin(x)")
(l2,) = ax.plot(x, np.cos(x), label="cos(x)")

lines = [l1, l2]

axcolor = "lightgoldenrodyellow"
rax = plt.axes([0.05, 0.4, 0.1, 0.15], facecolor=axcolor)
labels = [str(line.get_label()) for line in lines]
visibility = [line.get_visible() for line in lines]
check = CheckButtons(rax, labels, visibility)


def toggle(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    fig.canvas.draw_idle()


check.on_clicked(toggle)

plt.show()
