import networkx as nx  
import matplotlib.pyplot as plt 

g = nx.DiGraph()
 
g.add_edge('b', 'a') 
g.add_edge('b', 'd') 
g.add_edge('d', 'a') 
g.add_edge('a', 'c') 

nx.draw(g, with_labels = True, node_color='#00b4d9', node_size=700) 
plt.savefig("filename.png")