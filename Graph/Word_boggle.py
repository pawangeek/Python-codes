def findwords(board, i, j, dictionary, visited, string, ans):

    row, col = len(board), len(board[0])

    rnbr = [-1,-1,-1,0,0,1,1,1]
    cnbr = [-1,0,1,-1,1,-1,0,1]

    visited[i][j] = True
    string += board[i][j]

    for k in dictionary:
        if k==string:
            ans.append(string)

    for dx, dy in zip(rnbr, cnbr):
        
        x, y = i+dx, j+dy

        if (x>=0 and x<row and y>=0 and y<col and visited[x][y] is False):
            findwords(board, x, y, dictionary, visited, string, ans)

    visited[i][j] = False

def boggle(board, dictionary):

    row, col = len(board), len(board[0])

    visited = [[False for i in range(col)] for j in range(row)]
    ans = []

    for i in range(row):
        for j in range(col):
            findwords(board, i, j, dictionary, visited, '', ans)

    return ans

dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
board = [['G', 'I', 'Z'],
         ['U', 'E', 'K'],
         ['Q', 'S', 'E']]

print(boggle(board, dictionary))

# Time complexity : 
# For every cell there are 4 directions and there are N^2 cells. So the time complexity is O(8^(N^2))

# Space complexity :
# The maximum length of recursion can be N^2, where N is the side of the matrix. So it's O(N^2)