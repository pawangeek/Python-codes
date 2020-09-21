INF = float('inf')

graph = [ [0, 1, INF, INF], 
          [INF, 0, -1, INF], 
          [INF, INF, 0, -1], 
          [-1, INF, INF, 0]]

#             1
#     (0)----------->(1) 
#     /|\             | 
#      |              | 
#   -1 |              | -1 
#      |             \|/ 
#     (3)<-----------(2) 
#             -1

v = len(graph)
# Here comes v->4

def negcyclefllod(graph, v):

    dist = [[INF for i in range(v+1)] for j in range(v+1)]

    # dist = [[INF, INF, INF, INF, INF], 
    #         [INF, INF, INF, INF, INF], 
    #         [INF, INF, INF, INF, INF],
    #         [INF, INF, INF, INF, INF],
    #         [INF, INF, INF, INF, INF]]

    for i in range(v):
        for j in range(v):
            dist[i][j] = graph[i][j]

    for k in range(v):
        
        # Pick all vertices as source one by one 
        for i in range(v):

            # Pick all vertices as destination for the above picked source 
            for j in range(v):

                # If vertex k is on the shortest path from 
                # i to j, then update the value of dist[i][j]
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]

    for i in range(v):
        if dist[i][i]<0:
            return True

    return False

print(negcyclefllod(graph, v))