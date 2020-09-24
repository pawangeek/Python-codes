# Check that the same number is not present in the current row, current column and current 3X3 subgrid
# After checking for safety, assign the number, and recursively check whether this assignment leads to a solution or not
# If the assignment doesn’t lead to a solution, then try the next number for the current empty cell

def emptycell(grid, pos):

    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                pos[0], pos[1] = i, j
                return True

    return False

def safebox(grid, row, col, num):
    row -= row%3
    col -= col%3

    for i in range(row, row+3):
        for j in range(col, col+3):
            if num==grid[i][j]:
                return False
    
    return True


def safecol(grid, col, num):
    for i in range(9):
        if num==grid[i][col]:
            return False

    return True


def saferow(grid, row, num):

    for i in range(9):
        if num==grid[row][i]:
            return False
    
    return True

def safe_location(grid, row, col, num):
    return saferow(grid, row, num) and safecol(grid, col, num) and safebox(grid, row, col, num)

def solve(grid):

    pos = [0,0]

    if not emptycell(grid, pos):
        return True

    row, col = pos[0], pos[1]

    for num in range(1, 10):
        if safe_location(grid, row, col, num):

            grid[row][col] = num
            if solve(grid):
                return True

            grid[row][col] = 0

    return False

for _ in range(int(input())):
    grid = []
    
    for i in range(9):
        
        lst = map(int, input().split())
        grid.append(list(lst))

    if(solve(grid)): 
        for i in range(9):
            print(*grid[i])
