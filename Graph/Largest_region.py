class Graph:

    def __init__(self, row, col, g):
        self.col = col
        self.row = row
        self.graph = g

    def largestregion(self):

        visited = [[0 for i in range(self.col)] for j in range(self.row)]
        result = -1

        for i in range(self.row):
            for j in range(self.col):

                if self.graph[i][j] and not visited[i][j]:

                    count = [0]
                    self.dfs(i, j, visited, count)
                    result = max(result, count[0])

        return result

    def dfs(self, i, j, visited, count):

        rnbr = [-1, -1, -1,  0,  0,  1,  1,  1]
        cnbr = [-1,  0,  1, -1,  1, -1,  0,  1]

        if i>=self.row or i<0 or j>=self.col or j<0 or self.graph[i][j]==0:
            return

        self.graph[i][j] = 0
        count[0] += 1

        for k in range(8):
            self.dfs(i+rnbr[k], j+cnbr[k], visited, count)

graph = [[1, 1, 0, 0, 0], 
         [0, 0, 0, 0, 1], 
         [1, 0, 1, 1, 1], 
         [0, 1, 0, 1, 0], 
         [1, 0, 1, 0, 1]] 

row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)
print(g.largestregion())