class Graph:

    def __init__(self):
        self.graph = {}

    # Function to add edge in graph
    def addedge(self, u, v):

        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def bfs(self, s):

        # Mark all nodes as unvisited initially
        visited = [False]*len(self.graph)

        # Append the source in bfs
        queue = []
        queue.append(s)

        visited[s] = True

        while queue:

            s = queue.pop(0)
            print(s, end = ' -> ')

            for i in self.graph[s]:

                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True

        print(None)

if __name__ == "__main__":
    g = Graph()
    g.addedge(0, 1) 
    g.addedge(0, 2) 
    g.addedge(1, 2) 
    g.addedge(2, 0) 
    g.addedge(2, 3) 
    g.addedge(3, 3) 

    g.bfs(1)