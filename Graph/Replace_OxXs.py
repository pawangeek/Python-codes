mat =  [[ 'X', 'O', 'X', 'O', 'X', 'X' ],  
        [ 'X', 'O', 'X', 'X', 'O', 'X' ],  
        [ 'X', 'X', 'X', 'O', 'X', 'X' ],  
        [ 'O', 'X', 'X', 'X', 'X', 'X' ],  
        [ 'X', 'X', 'X', 'O', 'X', 'O' ],  
        [ 'O', 'O', 'X', 'O', 'O', 'O' ]]

# Function to change all occurances get all O instance from corner
def floodfill(i, j, mat):

    if i<0 or i>=len(mat) or j<0 or j>=len(mat[0]) or mat[i][j]!='-':
        return

    mat[i][j]='O'

    rnbr = [-1, 0, 0, 1]
    cnbr = [0, 1, -1, 0]

    for dx, dy in zip(rnbr, cnbr):
        floodfill(i+dx, j+dy, mat)

row = len(mat)
col = len(mat[0])

for i in range(row):   
    print(mat[i])

for i in range(row):
    for j in range(col):
        if mat[i][j]=='O':
            mat[i][j]='-'

# For left
for i in range(row):
    if mat[i][0]=='-':
        floodfill(i, 0, mat)

# For right
for i in range(row):
    if mat[i][col-1]=='-':
        floodfill(i, col-1, mat)

# For top
for i in range(col):
    if mat[0][i]=='-':
        floodfill(0, i, mat)

# For bottom
for i in range(col):
    if mat[row-1][i]=='-':
        floodfill(row-1, i, mat)

for i in range(row):
    for j in range(col):
        if mat[i][j]=='-':
            mat[i][j]='X'

for i in range(row):   
    print(mat[i])