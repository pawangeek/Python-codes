# Whose vertices can be divided into two disjoint sets

# If graph has many connected components and each component is bipartite
# Than graph is bipartite

# (i) It should be two colorable
# (ii) Not contain odd cycle

# IDEA : Assign each vertex the color differs from color of its parent in DFS

"""
Algorithm

1) Initially color all of them white

2) Pick a white vertex, color it red and check all of its neighbours
    2.1) If neightbours are white color them green
    2.2) And recursively check its neighbours

3) Repeat above step till all nodes are colored

4) During process if you find a neighbour vertex is already colored with same color
   Stop process and declare it not bipartite

"""

graph = [[1, 4, 5, 6], [], [0, 1, 2, 5], [0, 2, 4], [0, 1, 4], [1, 2, 3, 6], [2, 3]]
n = len(graph)
color = {}

def dfs(position):

    for i in graph[position]:

        # If color is same as parent than not bipartite
        if i in color:
            if color[i]==color[position]:
                return False

        # If not same than recursively check for it's child
        else:
            color[i] = 1-color[position]
            if not dfs(i):
                return False

    return True

f=0

for i in range(n):

    # If not yet colored, color it with 0
    if i not in color:

        color[i]=0
        if not dfs(i):
            f=1
            break
    
print(1) if f==0 else print(0)

# Time complecity = O(v^2)