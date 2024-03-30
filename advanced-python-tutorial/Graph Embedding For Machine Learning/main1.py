# pip install karateclub networkx numpy matplotlib

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from karateclub.node_embedding.neighbourhood.deepwalk import DeepWalk

G = nx.random_tree(40)

nx.draw_spring(G)
plt.show()

deepwalk = DeepWalk(dimensions=2)
deepwalk.fit(G)

embedding = deepwalk.get_embedding()
print(embedding)

fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(projection="3d")
ax.scatter(embedding[:, 0], embedding[:, 1], embedding[:, 2])
plt.show()
