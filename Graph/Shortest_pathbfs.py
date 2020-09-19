from collections import defaultdict, deque


def addEdge(graph,u,v): 
    graph[u].append(v) 
    graph[v].append(u)

def BFS (graph, sour, dest, pred, dist, v):

    # queue to maintain queue of vertices whose 
    # adjacency list is to be scanned as per normal DFS algorithm 
    queue = deque()

    # boolean array visited[] which stores the 
    # information whether ith vertex is reached 
    # at least once in the Breadth first search 
    visited = [False]*v

    # now source is first to be visited and 
    # distance from source to itself should be 0 
    visited[sour]=True
    dist[sour] = 0

    queue.append(sour)

    while queue:
        u = queue.popleft()

        for i in graph[u]:
            if not visited[i]:
                visited[i] = True

                # Increase dist by 1 and store predessor in pred
                # to get path at last
                dist[i] = dist[u]+1
                pred[i] = u

                queue.append(i)

                # We stop BFS when we find destination. 
                if i==dest:
                    return True

    return False

def printshort(graph, sour, dest, v):

    # predecessor[i] array stores predecessor of 
    # i and distance array stores distance of i from s 

    # initially all vertices are unvisited  so v[i] for all i is false 
    # and as no path is yet constructed dist[i] for all i set to infinity 
    pred = [-1]*v
    dist = [float('inf')]*v

    if BFS( graph, sour, dest, pred, dist, v ) is False:
        print ("Given source and dest not connected")

    print(dist)
    print(pred)

    print("Shortest path length is : " +  str(dist[dest]))

    path = []
    path.append(dest)

    while pred[dest]!=-1:
        path.append(pred[dest])
        dest = pred[dest]

    print(path[::-1])
    
v = 8
g1 = defaultdict(list)

addEdge(g1,0, 1)
addEdge(g1,0, 3)
addEdge(g1,1, 2) 
addEdge(g1,3, 4) 
addEdge(g1,3, 7) 
addEdge(g1,4, 5) 
addEdge(g1,4, 6)
addEdge(g1,4, 7) 
addEdge(g1,5, 6) 
addEdge(g1,6, 7) 

printshort(g1, 0, 7, v)
