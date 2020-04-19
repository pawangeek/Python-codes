# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3303/
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

if not grid:
    return 
        
m,n = len(grid), len(grid[0])
        
for i in range(1,n):
    grid[0][i] += grid[0][i-1]
            
for i in range(1,m):
    grid[i][0] += grid[i-1][0]
            
for i in range(1,m):
    for j in range(1,n):
        grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i][j-1])
                
print (grid[-1][-1])