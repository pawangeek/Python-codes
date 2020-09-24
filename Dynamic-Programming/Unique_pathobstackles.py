def uniquePathsWithObstacles(self, grid):
    
    m = len(grid)
    n = len(grid[0])
    
    # This is added for case when our starting or ending point is zero
    if grid[0][0]==1 or grid[m-1][n-1]==1:
        return 0

    dp = [[0 for i in range(n)] for i in range(m)]
    dp[0][0] = 1
    
    print(dp)

    # We do dp[i][0] = dp[i-1][0] since dp[i][0] = 1 fails at testcase 
    # [[0,1,0] We have to depend on previous state
    #  [0,1,0]]

    for i in range(1,m):
        if grid[i][0]==0:
            dp[i][0] = dp[i-1][0]
            
    print(dp)

    for i in range(1,n):
        if grid[0][i]==0:
            dp[0][i] = dp[0][i-1]

    for i in range(1,m):
        for j in range(1,n):

            if grid[i][j]==0:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
                
    print(dp)
    
    return (dp[m-1][n-1])
    