from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices

    # Function to add edge in graph
    def addedge(self, u, v):
        self.graph[u].append(v) 

    def toposort(self):

        visited = [False]*self.v
        stack = []
        
        for i in range(self.v):
            if visited[i] is False:
                self.topoutil(visited, i, stack)

        print(*(stack[::-1]))

    def topoutil(self, visited, v, stack):

        visited[v]=True

        for i in self.graph[v]:
            if visited[i] is False:
                self.topoutil(visited, i, stack)

        stack.append(v)

if __name__ == "__main__":

    g = Graph(6)
    g.addedge(5, 2)
    g.addedge(5, 0)
    g.addedge(4, 0)
    g.addedge(4, 1)
    g.addedge(2, 3)
    g.addedge(3, 1) 

    g.toposort()