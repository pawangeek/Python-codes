from collections import defaultdict

# We do DFS traversal of the given graph. 

# In DFS tree an edge (u, v) (u is parent of v in DFS tree) is bridge if 
# there does not exist any other alternative to reach u or an ancestor of u from subtree rooted with v

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices
        self.time = 0

    def addedge(self, u, v):
        self.graph[u].append(v)

    def bridges(self):

        visited = [False]*self.v
        desc = [float('inf')]*self.v
        low = [float('inf')]*self.v

        parent = [-1]*self.v

        for i in range(self.v):
            if visited[i] is False:
                self.bridgeutil(i, visited, parent, low, desc)

    def bridgeutil(self, v, visited, parent, low, desc):

        """
        u           --> The vertex to be visited v 
        visited[]   --> keeps tract of visited vertices 
        disc[]      --> Stores discovery times of visited vertices 
                    --> (Indicate the dicovery time of node)
        low[]       --> Indicate whether there's some early node that can be visited by subtree rooted with that node
        parent[]    --> Stores parent vertices in DFS tree

        """

        visited[v] = True

        desc[v] = self.time
        low[v] = self.time

        self.time += 1

        for i in self.graph[v]:

            if visited[i] is False:
                parent[i] = v
                self.bridgeutil(i, visited, parent, low, desc)

                # Check if the subtree rooted with i has a connection to 
                # one of the ancestors of v 
                low[v] = min(low[v], low[i])

                # If the lowest vertex reachable from subtree 
                # under i is below v in DFS tree, then v-i is a bridge
                if low[i]>desc[v]:
                    print(v,i)

            # Update low value of v for parent function calls
            elif i != parent[v]:
                low[v] = min(low[v], desc[i])

g1 = Graph(5) 
g1.addedge(1, 0) 
g1.addedge(0, 2) 
g1.addedge(2, 1) 
g1.addedge(0, 3) 
g1.addedge(3, 4) 

g1.bridges()

# Time complexity:
#   The above function is simple DFS with additional arrays. 
#   So time complexity is same as DFS which is O(V+E)