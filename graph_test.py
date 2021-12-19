import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
L = [(0, 1), (1, 2), (2, 4), (3, 4), (4, 5), (5, 2), (4, 1)]
G.add_edges_from(L)
nx.draw(G, with_labels=1)
plt.show()
