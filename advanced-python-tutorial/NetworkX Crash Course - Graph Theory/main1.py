import networkx as nx
import matplotlib.pyplot as plt

edge_list = [(1,2), (2,3), (3,4), (3,5), (4,6), (6,7)]

G = nx.Graph()
G.add_edges_from(edge_list)

print(nx.shortest_path(G, 2, 4))

nx.draw_spring(G, with_labels=True)
plt.show()

nx.draw_circular(G, with_labels=True)
plt.show()

nx.draw_shell(G, with_labels=True)
plt.show()

nx.draw_spectral(G, with_labels=True)
plt.show()

nx.draw_random(G, with_labels=True)
plt.show()

nx.draw_planar(G, with_labels=True)
plt.show()

