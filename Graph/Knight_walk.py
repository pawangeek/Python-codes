# find out the minimum steps a Knight will take to reach the target position.

"""
1. Create an empty queue and enqueue source cell having
   distance 0 from source (itself)
 
2. loop till queue is empty
 
   a) Pop next unvisited node from queue
 
   b) If the popped node is destination node, return its distance
 
   c) Else we mark current node as visited and for each of 8 possibl movements for a knight, 
      we enqueue each valid movement into the queue with +1 distance 
      (min distance of given node from source = min distance of parent from source + 1)

"""


from collections import deque

knightpos = [3,4]
targetpos = [0,0]

n = 6 # board n*n

rnbr = [2, 2, -2, -2, 1, 1, -1, -1]
cnbr = [1, -1, 1, -1, 2, -2, 2, -2]

queue = deque()
queue.append(knightpos+[0])

# Create a visited array and mark source position as visited
visited = [[False for i in range(n)] for j in range(n)]
visited[knightpos[0]][knightpos[1]] = True 

while queue:

    x,y,dist = queue.popleft()

    # If reach destination stop and return dist
    if x==targetpos[0] and y==targetpos[1]:
        print(dist)
        break
    
    # Else append all possible 8 steps of knight (only valid one)
    for i,j in zip(rnbr, cnbr):
        dx = x+i
        dy = y+j

        if dx>=0 and dx<n and dy>=0 and dy<n and not visited[dx][dy]:
            visited[dx][dy] = True
            queue.append([dx, dy, dist+1])


# Time complexity: O(N^2).
#       At worst case, all the cells will be visited so time complexity is O(N^2).

# Auxiliary Space: O(N^2).
#       The nodes are stored in queue. So the space Complexity is O(N^2).