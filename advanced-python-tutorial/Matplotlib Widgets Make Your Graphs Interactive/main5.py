import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox


fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1])

ax_box = plt.axes([0.1, 0.05, 0.8, 0.075], facecolor="lightgoldenrodyellow")
text_box = TextBox(ax_box, "title: ", initial="sample plot")


def submit(text):
    ax.set_title(text)
    fig.canvas.draw_event()


text_box.on_submit(submit)

plt.show()
