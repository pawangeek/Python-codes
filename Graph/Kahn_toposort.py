# Topo sort -> It is a linear ordering of vertices in a Directed Acyclic Graph (DAG)
# When possible : When there is no cycle (else it's become a loop)

# Necessary condition : Atleast one node with inorder node = 0 (Else it's loop)

# Practical Implementation : Another neat thing to know: Cycle detection/topo-sorting is a very 
#                            important task in network theory, for detecting redundancies, faulty nodes

from collections import defaultdict

class Graph:
    def __init__ (self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices

    def addedge(self, u, v):
        self.graph[u].append(v)

    def kahnsort(self):

        # Initialize all indegrees as 0
        in_degree = [0]*self.v

        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j]+=1

        queue = []
        for i in range(self.v):
            if in_degree[i] == 0:
                queue.append(i)

        order, cnt = [], 0

        while queue:

            u = queue.pop(0)
            order.append(u)

            for i in self.graph[u]:
                in_degree[i] -= 1

                if in_degree[i]==0:
                    queue.append(i)

            cnt += 1

        if cnt != self.v:
            print("Cycle")
        else:
            print(*(order))

if __name__ == "__main__":
    g = Graph(6) 
    g.addedge(5, 2) 
    g.addedge(5, 0) 
    g.addedge(4, 0) 
    g.addedge(4, 1) 
    g.addedge(2, 3) 
    g.addedge(3, 1) 

    g.kahnsort()

# 1. Instantiate a Queue
# 2. Loop through your list of graph nodes, and enqueue all the nodes that have an in-degree = 0, 
#    in the queue that you just made above.

# 3. Outer loop: Start looping through your queue, pop top. The top node is the “current” node.

# 4. Inner Loop: For each neighbor of the “current” node, reduce the in-degree of that neighbor 1. 
#    Why are we doing this? Because we are removing the “current” node, from the graph. 
#    Duh!! At the same time, in the same inner loop, enqueue any “neighbor” with an in-degree of 0. 
#    This means that “neighbor” node is no longer dependent on anybody and thus a candidate to be in toposort.

# 5. Rinse, wash, repeat. Until you have your final topological sort.

# Time Complexity: O(V+E).
# The outer for loop will be executed V(vertices) number of times and 
# the inner for loop will be executed E(Edges) number of times.

# Auxillary Space: O(V).
# The queue needs to store all the vertices of the graph. So the space required is O(V)#