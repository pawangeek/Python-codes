import networkx as nx  
import matplotlib.pyplot as plt 

g = nx.DiGraph()

g.add_edge(5, 2) 
g.add_edge(5, 0) 
g.add_edge(4, 0) 
g.add_edge(4, 1) 
g.add_edge(2, 3) 
g.add_edge(3, 1) 
nx.draw(g, with_labels = True) 
plt.savefig("filename.png")