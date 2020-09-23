"""
ALGORITHM

1. Start DFS(G, v) from a random vertex v of the graph G. 

    (i)  If DFS(G, v) fails to reach every other vertex in the graph G, then there is some vertex u, 
         such that there is no directed path from v to u, and thus G is not strongly connected. 
    (ii) If it does reach every vertex, then there is a directed path from v to every other vertex in the graph G.

2. Reverse the direction of all edges in the directed graph G.

3. Again run a DFS starting from vertex v. 
    (i) If the DFS fails to reach every vertex, then there is some vertex u, 
        such that in the original graph there is no directed path from u to v. 
        
    (ii) On the other hand, if it does reach every vertex, then in the original graph there is a 
        directed path from every vertex u to v. Thus if G passes both DFS, it is strongly connected.

"""

from collections import defaultdict

class Graph:

    def __init__ (self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def addedge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited):

        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if visited[i] is False:
                self.dfs(i, visited)

    def fill(self, v, visited, stack):

        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.fill(i, visited, stack)

        stack.append(v)

    def ssc(self):

        visited = [False]*self.v
        stack = []

        for i in range(self.v):
            if visited[i] is False:
                self.fill(i, visited, stack)

        # For finding transpose of graph
        # (Transpose means reversing all edges of graph)
        
        g = Graph(self.v)
 
        for i in self.graph:
            for j in self.graph[i]:
                g.addedge(j,i)

        visited = [False]*self.v

        while stack:
            i = stack.pop()
            if visited[i] is False:
                g.dfs(i, visited)
                print()

if __name__ == "__main__":
    g1 = Graph(5)

    g1.addedge(1, 0) 
    g1.addedge(0, 2) 
    g1.addedge(2, 1) 
    g1.addedge(0, 3) 
    g1.addedge(3, 4) 

    g1.ssc()

# Time: The above algorithm calls DFS, finds reverse of the graph and again calls DFS. 
#       DFS takes O(V+E) for a graph represented using adjacency list.