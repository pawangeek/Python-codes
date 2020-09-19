from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self, u, v):
        self.graph[u].append(v)

    def dfs(self,s):

        visited = [False]*len(self.graph)
        self.dfsutil(visited, s)

        print(None)

    def dfsutil(self, visited, u):

        visited[u] = True
        print(u, end = ' -> ')

        for v in self.graph[u]:
            if visited[v] is False:
                self.dfsutil(visited, v)

if __name__ == '__main__':

    g = Graph()

    g.addedge(0, 1) 
    g.addedge(0, 2) 
    g.addedge(1, 2) 
    g.addedge(2, 0) 
    g.addedge(2, 3) 
    g.addedge(3, 3) 

    g.dfs(2)