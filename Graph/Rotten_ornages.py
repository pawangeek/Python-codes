from collections import deque

class Graph:

    def __init__(self, row, col, g):
        self.row = row
        self.col = col
        self.graph = g

    def rottenoranges(self):

        fresh = 0
        rotten = deque()

        for i in range(self.row):
            for j in range(self.col):

                if self.graph[i][j]==2:
                    rotten.append((i, j))

                if self.graph[i][j]==1:
                    fresh+=1

        path = [(1,0), (-1,0), (0,-1), (0,1)]
        minutes = 0

        while rotten and fresh>0:

            minutes+=1

            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                for i, j in path:
                    
                    dx = x+i
                    dy = y+j

                    if dx<0 or dx>=self.row or dy<0 or dy>=self.col:
                        continue

                    if self.graph[dx][dy]==0 or self.graph[dx][dy]==2:
                        continue

                    fresh-=1
                    self.graph[dx][dy] = 2

                    rotten.append((dx, dy))

        return minutes if fresh==0 else -1

if __name__ == '__main__':

    graph = [[2, 1, 0, 2, 1 ], 
             [1, 0, 1, 2, 1 ], 
             [1, 0, 0, 2, 1 ]]

    g = Graph(3, 5, graph)
    print(g.rottenoranges())
