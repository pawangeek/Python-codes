"""
PSEUDOCODE

Begin
   if (x,y) is the bottom right corner, then
      mark the place as 1
      return true

   if isValidPlace(x, y) = true, then
      mark (x, y) place as 1

      if solveRatMaze(x+1, y) = true, then //for forward movement
         return true

      if solveRatMaze(x, y+1) = true, then //for down movement
         return true

      mark (x,y) as 0 when backtracks
      return false
      
   return false
End

"""

def solvemaze(maze, x, y, sol):

    # if (x, y is goal) and we reached we got our solution (Base case)
    if x==n-1 and y==n-1 and maze[x][y]==1:
        sol[x][y] = 1
        return True
    
    print(sol)
    # Check if postion is valid or not
    if x>=0 and x<n and y>=0 and y<n and maze[x][y]==1:
        sol[x][y] = 1

        # Move horizontally if safe
        if solvemaze(maze, x+1, y, sol):
            return True

        # Move vertically if horizontally not safe and check vertically is safe or not
        if solvemaze(maze, x, y+1, sol):
            return True

        # If none of the above movements work then  
        # BACKTRACK: unmark x, y as part of solution path 
        sol[x][y] = 0
        return False

n = 4
sol = [[0 for i in range(n)] for j in range(n)]

maze = [[1, 0, 0, 0], 
        [1, 1, 0, 1], 
        [0, 1, 0, 0], 
        [1, 1, 1, 1]] 

if not solvemaze(maze, 0, 0, sol):
    print("No solution")
else:
    for i in range(n):
        print(*(sol[i]))