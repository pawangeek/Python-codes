# @Date:   2020-05-03T21:26:50+05:30
# @Last modified time: 2020-05-03T21:33:59+05:30

# https://leetcode.com/contest/weekly-contest-187/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

nums = [8,2,4,7]
limit = 4

n, res, dp = len(nums), 1, [-1]*len(nums)

for i in range(n):
    mn, mx, dp[i] = nums[i], nums[i], 0

    if(i-1+res >= n):
        break

    for j in range(i+1,n):

        c1 = abs(nums[j]-mn)
        c2 = abs(nums[j]-mx)

        dp[j] = max(dp[j-1], max(c1,c2))

        if(dp[j] <= limit):
            res = max(res, j-i+1)
        else:
            break

        if(nums[j] > mx):
            mx = nums[j]
        if(nums[j] < mn):
            mn = nums[j]

print (res)
