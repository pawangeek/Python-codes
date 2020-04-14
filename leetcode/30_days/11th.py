import heapq

# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3297/
# Last Stone Weight

# We have a collection of stones, each stone has a positive integer weight.
# Each turn, we choose the two heaviest stones and smash them together. 

# Suppose the stones have weights x and y with x <= y.  The result of this smash is:
# * If x == y, both stones are totally destroyed;
# * If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

stones = [2,7,4,1,8,1]

stones = [-val for val in stones]
heapq.heapify(stones)

while len(stones) > 1:
    x1 = heapq.heappop(stones)
    x2 = heapq.heappop(stones)

    # Condition when both stones are equal
    if x1 != x2:
        heapq.heappush(stones,-abs(x1-x2))
    
if len(stones) == 0:
    print(0)
else:
	print(-stones[0])