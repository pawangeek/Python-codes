# https://leetcode.com/contest/biweekly-contest-24/problems/restore-the-array/

s,k = "1317",2000

l = len(s)
dp = [0]*l
        
dp[-1]=1 if 0<int(s[-1])<=k else 0
        
for i in range(l-2,-1,-1):
            
    # if starting with 0 leave
    if s[i] == '0':
        continue
            
    if len(s)-i <= len(str(k)) and int(s[i:]) <= k:
        dp[i] = 1
                
    for j in range(i+1, l):
        if int(s[i:j]) > k:
            break
                    
        dp[i] = (dp[i]+dp[j]) % int(1e9 + 7)
                
print (dp[0])  