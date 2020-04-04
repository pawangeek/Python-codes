# Given two natural number n and m. 
# The task is to find the number of ways
# In which the numbers that are greater than or equal to m can be added to get the sum n.

MAX = 100
import numpy as np 

n,m = map(int,input().split())

dp = np.zeros((n+2,n+2))
dp[0][n+1] = 1

for k in range(n, m - 1, -1) : 
  
    # i is for sum 
    for i in range(n + 1) : 
  
        # initializing dp[i][k] to number ways to get sum using numbers greater than or equal k+1 
        dp[i][k] = dp[i][k + 1] 
  
        # if i > k 
        if (i - k >= 0) : 
            dp[i][k] = (dp[i][k] + dp[i - k][k]) 

print(dp)
print(dp[n][m])