w1 = 'mamta'
w2 = 'kavita'

m, n = len(w1), len(w2)
dp = [[0 for i in range(m+1)] for j in range(n+1)]
            
for i in range(n+1):
    for j in range(m+1):
        
        if i==0 or j==0:
            dp[i][j]=max(i,j)
        
        elif w2[i-1]==w1[j-1]:
            dp[i][j] = dp[i-1][j-1]
            
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1


print(dp)        
print (dp[-1][-1])