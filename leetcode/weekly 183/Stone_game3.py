# https://leetcode.com/contest/weekly-contest-183/problems/stone-game-iii/
# Difficulty, concept = Hard, Dynamic programming

stoneValue = [1,2,3,7]

# start from the end
stoneValue.reverse()
n = len(stoneValue)

# initialize to min
# dp[i] means: for stoneValue of length i + 1, what's the max score I can get with me starting first 
dp, prev = [float('-inf') for i in range(n)], []

# build pre sum array
total = 0
for v in stoneValue:
    total += v
    prev.append(total)
            
for i in range(n):

    # special case that I can grab all stones
    if i in [0, 1, 2]:
        curr = sum(stoneValue[:i + 1])
        dp[i] = curr
                
    # try grab 1, 2, 3 stones to get max
    for n in [1, 2, 3]:
        if i >= n:
            curr = sum(stoneValue[i - n + 1:i + 1])
            dp[i] = max(dp[i], prev[i - n] - dp[i - n] + curr)

res = dp[len(stoneValue) - 1]
# Alice win if got more than half of the score

if res * 2 > total:
    print ('Alice')
elif res * 2 == total:
    print ('Tie')
else:
    print ('Bob')