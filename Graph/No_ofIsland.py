class Graph:

    def __init__(self,row, col, g):
        self.row = row
        self.col = col
        self.graph = g

    def dfs(self, i, j):
    
        if i>=self.row or i<0 or j>=self.col or j<0 or self.graph[i][j]!=1:
            return

        self.graph[i][j]=0

        rownbr = [-1, -1, -1,  0, 0, 1, 1,  1]
        colnbr = [-1,  0,  1, -1, 1, 1, 0, -1]

        for k in range(8):
            self.dfs(i+rownbr[k], j+colnbr[k])

    def islands(self):

        count = 0

        for i in range(self.row):
            for j in range(self.col):

                if self.graph[i][j]==1:
                    self.dfs(i, j)
                    count+=1

        return count

graph = [[1, 1, 0, 0, 0], 
         [0, 0, 0, 0, 1], 
         [1, 0, 0, 1, 1], 
         [0, 0, 0, 0, 0], 
         [1, 0, 1, 0, 1]] 

row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)
print(g.islands())