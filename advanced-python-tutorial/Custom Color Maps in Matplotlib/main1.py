import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import seaborn as sns

data = sns.load_dataset("titanic")

custom_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("custom", ["#00aabb", "#ffffff", "#ff7777"])

sns.heatmap(data.corr(), cmap=custom_cmap, annot=True, vmin=-1, vmax=1)
plt.show()