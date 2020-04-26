# @Date:   2020-04-26T23:31:29+05:30
# @Last modified time: 2020-04-26T23:35:49+05:30

# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

# Prefix-Suffix sum Method

cardPoints = [1,2,3,4,5,6,1]
k = 3    

n  =  len(cardPoints)

presum  = [0]*(n+1)
sufsum  = [0] * (n+1)

for  i  in  range(1, n+1):
    presum[i] = presum[i-1] + cardPoints[i-1]
    sufsum[i] = sufsum[i-1] + cardPoints[n-i]

sums = 0
for x in range(k+1):
    sums = max(sums,presum[x]+sufsum[k-x])

print (sums)
