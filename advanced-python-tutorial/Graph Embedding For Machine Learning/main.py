# pip install karateclub networkx numpy matplotlib

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from karateclub.node_embedding.neighbourhood.deepwalk import DeepWalk

G = nx.random_tree(40)

nx.draw_spring(G)
plt.show()

