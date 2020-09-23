# What is the maximum number of edges they can add so that graph id still bipartite?

# Let the number of nodes in the left set be l and the number of nodes in the right set be r, 
# The maximum number of edges that can exist is l * r, but n - 1 edges already exist 
# so the maximum number of edges to be added is l * r - (n - 1).

count = [0]*2
n = int(input())
graph = [[] for _ in range(n + 1)]

# Adding edges in both sides so that in become undirected
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

stack = [(1,0,0)]

while stack:

    node, parent, color = stack.pop()

    count[color]+=1
    for i in graph[node]:
        if i!=parent:
            stack.append((i, node, 1-color))

print((count[0]*count[1])-(n-1))