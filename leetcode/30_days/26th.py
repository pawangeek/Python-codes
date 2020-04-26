# @Date:   2020-04-26T23:44:26+05:30
# @Last modified time: 2020-04-26T23:48:58+05:30

# https://leetcode.com/problems/longest-common-subsequence/
# Standard DP Problem

s1, s2 = "abcde", "ace"
m, n = len(s1), len(s2)

dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

for row in range(1, m+1):
    for col in range(1, n+1):

        if s1[row-1] == s2[col-1]:
            dp[row][col] = 1 + dp[row-1][col-1]

        else:
            dp[row][col] = max(dp[row][col-1], dp[row-1][col])

print (dp[m][n])
