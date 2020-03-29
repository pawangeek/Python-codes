# https://leetcode.com/contest/weekly-contest-182/problems/count-number-of-teams/
# Concept: DP(Number of increasing subs of len k)

# Difficulty : Medium

import math as mt

class Solution:
    
    def numTeams(self, rating) -> int:
        
        arr = rating
        n = len(arr)
        k = 3
        
        dp = [[0 for i in range(n)]  
             for i in range(k)] 
               
        for i in range(n): 
            dp[0][i] = 1
   
        for l in range(1, k): 
            for i in range(l, n): 

                dp[l][i] = 0
                for j in range(l - 1, i): 
                    if (arr[j] < arr[i]): 
                        dp[l][i] += dp[l - 1][j] 
              
        Sum = 0
        for i in range(k - 1, n): 
            Sum += dp[k - 1][i] 
            
        arr = rating[::-1]
        n = len(arr)
        k = 3
        
        dp = [[0 for i in range(n)]  
             for i in range(k)] 
               
        for i in range(n): 
            dp[0][i] = 1
   
        for l in range(1, k): 
            for i in range(l, n): 

                dp[l][i] = 0
                for j in range(l - 1, i): 
                    if (arr[j] < arr[i]): 
                        dp[l][i] += dp[l - 1][j] 
              
        Sum2 = 0
        for i in range(k - 1, n): 
            Sum2 += dp[k - 1][i] 
            
        return (Sum+Sum2)