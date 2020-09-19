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
        stack = [False]*self.v

        for i in range(self.v):

            # Don't recur if already visited it
            if visited[i] is False:
                if self.dfsutil(i, visited, stack):
                    return True

        return False

    def dfsutil(self, vertex, visited, stack):

        # Mark current node as visited
        visited[vertex] = True
        stack[vertex] = True

        for i in self.graph[vertex]:

            # Recur for all neighbour
            if visited[i] is False:
                if self.dfsutil(i, visited, stack):
                    return True
            
            # If any neighbour is visited and present in stack
            # Than there is a cycle
            elif stack[i] is True:
                return True

        # The node needs to be removed before function ends
        stack[vertex] = False
        return False

if __name__ == "__main__":
    g = Graph(4)
    g.addedge(0, 1) 
    g.addedge(0, 2) 
    g.addedge(1, 2) 
    g.addedge(2, 0) 
    g.addedge(2, 3) 
    g.addedge(3, 3) 

    print(g.iscycle())