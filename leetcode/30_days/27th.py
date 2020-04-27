# @Date:   2020-04-27T21:36:11+05:30
# @Last modified time: 2020-04-27T21:39:49+05:30



# Explanation : https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach
# Problem : https://leetcode.com/problems/maximal-square/

# Given a 2D binary matrix filled with 0's and 1's,
# find the largest square containing only 1's and return its area.

# Dp problem
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

if matrix is None or len(matrix) < 1:
    print (0)

rows = len(matrix)
cols = len(matrix[0])

dp = [[0]*(cols+1) for _ in range(rows+1)]
max_side = 0

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == '1':
            dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
            max_side = max(max_side, dp[r+1][c+1])

print (max_side * max_side)
