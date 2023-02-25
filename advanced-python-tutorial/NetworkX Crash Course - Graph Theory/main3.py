import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.complete_graph(5)
G2 = nx.complete_graph(5)
G2 = nx.relabel_nodes(G2, {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"})
G_connector = nx.from_edgelist([(4, "X"), ("X", "A")])

G = nx.compose_all([G1, G2, G_connector])

print(nx.degree_centrality(G))
print(nx.betweenness_centrality(G))

print(nx.density(G))
print(nx.diameter(G))
print(list(nx.eulerian_path(G)))
print(list(nx.find_cliques(G)))
print(list(nx.bridges(G)))
print(list(nx.local_bridges(G)))

nx.draw_spring(G, with_labels=True)
plt.show()
