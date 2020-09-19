class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.graph = {}

    # Function to add edge in graph
    def addedge(self, u, v):

        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def iscycle(self):

        # Mark all nodes as unvisited
        visited = [False]*self.v

        for i in range(self.v):

            # Don't recur if already visited it
            if visited[i] is False:
                if self.dfsutil(i, visited, -1):
                    return True

        return False

    def dfsutil(self, vertex, visited, parent):

        # Mark current node as visited
        visited[vertex] = True

        for i in self.graph[vertex]:

            if visited[i] is False:
                if self.dfsutil(i, visited, vertex):
                    return True
            
            # If adjacant vertex is visited and not parent of current vertex
            # Than there is a cycle
            elif parent != i:
                return True

        return False

if __name__ == "__main__":
    g = Graph(4)
    g.addedge(0, 1) 
    g.addedge(0, 2) 
    g.addedge(1, 0) 
    g.addedge(2, 0) 
    g.addedge(2, 3) 
    g.addedge(3, 3) 

    print(g.iscycle())