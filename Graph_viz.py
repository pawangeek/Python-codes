import networkx as nx  
import matplotlib.pyplot as plt 

g = nx.DiGraph()

g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 0) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3)

nx.draw(g, with_labels = True) 
plt.savefig("filename.png")