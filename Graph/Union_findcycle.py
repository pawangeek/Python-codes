"""
ALGORITHM

1. Makes a new set by creating a new element with a parent pointer to itself.

2. Then process each edge of the graph and perform find and Union operations 
   to make subsets using both vertices of the edge.

3. If find operation on both the vertices returns the same parent 
   (means both vertices belongs to the same subset) then cycle is detected.

"""

from collections import defaultdict

class Graph:

    def __init__ (self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)
    
    def addedge(self, u, v):
        self.graph[u].append(v)

    def findparent(self, parent, i):

        if parent[i]==-1:
            return i
        else:
            return self.findparent(parent, parent[i])

    def union(self, parent, x, y):

        xp = self.findparent(parent, x)
        yp = self.findparent(parent, y)

        parent[xp] = yp

    def iscyclic(self):

        # Initialize all subsets as single element sets (All are parents)
        parent = [-1]*self.v

        # Iterate through all edges of graph, find subset of both 
        # vertices of every edge, if both subsets are same, then 
        # there is cycle in graph. 
        for i in self.graph:
            for j in self.graph[i]:

                x = self.findparent(parent, i)
                y = self.findparent(parent, j)

                if x==y:
                    return True
                
                self.union(parent, x, y)

        return False

if __name__ == "__main__":

    g = Graph(3)

    g.addedge(0,1)
    g.addedge(1,2)
    g.addedge(2,0)

    print("CYCLE") if g.iscyclic() else print("No CYCLE")
        
# Here implementation of union() and find() is naive and takes O(n) time in worst case