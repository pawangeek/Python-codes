s1 = 'dbbca'
s2 = 'aabc'

l1, l2 = len(s1), len(s2)
i1 = 'aadbbcbca'

dp = [[False for i in range(l2+1)] for j in range(l1+1)]

if l1+l2!=len(i1):
    print("False")

for i in range(l1+1):
    for j in range(l2+1):

        if i==0 and j==0:
            dp[i][j] = True

        elif s1[i-1]==i1[i+j-1] and s2[j-1]!=i1[i+j-1]:
            dp[i][j] = dp[i-1][j]

        elif s1[i-1]!=i1[i+j-1] and s2[j-1]==i1[i+j-1]:
            dp[i][j] = dp[i][j-1]

        elif s1[i-1]==i1[i+j-1] and s2[j-1]==i1[i+j-1]:
            dp[i][j] = dp[i][j-1] or dp[i-1][j]


for i in dp:
    print(i)