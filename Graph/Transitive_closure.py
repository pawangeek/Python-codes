# Given a directed graph, find out if a vertex v is reachable by vertex u
# Reachable means path from u->v

"""
IDeA

* Initialize all entries in adjacancy matrix as 0
* Call DFS for every node of graph to mark reachability
    -> We don't call DFS if already visited by it
"""

from collections import defaultdict

class Graph:

    def __init__(self, vert):
        self.v = vert
        self.graph = defaultdict(list)
        self.closure = [[0 for i in range(vert)] for j in range(vert)]

    def addedge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, s, v):

        # Mark reachability from itself
        self.closure[s][v]=1

        for i in self.graph[v]:
            if self.closure[s][i]==0:
                self.dfs(s, i)

    def transitiveclosure(self):

        for i in range(self.v):
            self.dfs(i, i)

        for i in self.closure:
            print(*(i))


if __name__ == "__main__":

    g = Graph(4) 
    g.addedge(0, 1) 
    g.addedge(0, 2) 
    g.addedge(1, 2) 
    g.addedge(2, 0) 
    g.addedge(2, 3) 
    g.addedge(3, 3)

    g.transitiveclosure()
