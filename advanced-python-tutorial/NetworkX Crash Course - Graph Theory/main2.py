import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

G = nx.from_numpy_array(np.array([[0,1,0],
                                  [1,1,1],
                                  [0,0,0]]))

nx.draw_spring(G, with_labels=True)
plt.show()
