# Backtrack is a method to solve problems by making a series of choices that we can return
# Backtrack used when we have many decision points

# The call stack remembers as choices and knows what to choose not

"""
Algorithm

1. Begin with the left-most column.

2. For every row in the column:
    2.1. Try placing the queen such that it cannot attack the queen in the previous columns.
    2.2. If such a placement is possible, add this cell to the solution set and recursively 
         check if this leads to a solution by calling the function on the subsequent column. If it does, return one.
    2.3. Else, remove this cell from the solution set.

3. Backtrack to the previous column by returning zero if no solution exists after the completion of step 2.

Stop the recursion when all the queens are placed.
"""

def issafe(board, row, col, N):

    for i in range(col):
        if board[row][i]==1:
            return False
    
    for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]==1:
            return False

    for i,j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]==1:
            return False

    return True

def solveutil(board, col, N):

    # Base case if all queens are placed
    if col>=N:
        return True

    for i in range(N):

        if issafe(board,i,col,N):

            # Place queen here
            board[i][col]=1

            # Recur for rest places
            if solveutil(board, col+1, N) is True:
                return True

            # If it doesn't form solution
            # Remove that placement
            board[i][col] = 0

    # If queen can't be placed in any row in this col
    return False

N = 8
board = [[0 for i in range(N)] for j in range(N)]
solveutil(board,0, N)

for i in range(N):
    print(*(board[i]))