# @Date:   2020-04-30T17:31:03+05:30
# @Last modified time: 2020-04-30T17:33:56+05:30

# https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1
# compute how much water it is able to trap after raining.

# To get the highest ground level on its left side
# we iterate through the heights array from left to right
# save the maximum value of the current ground level
# the previous highest ground level in another array, saying the left bounds array.

heights = [0,1,0,2,1,0,1,3,2,1,2,1]

# If len of heights is 1,2 no water can be filled
if not heights or len(heights) < 3:
    print (0)

# Now create a left bound and right bound array
size = len(heights)
lBound = [0] * size
rBound = [0] * size

# fill left bounds array
h = heights[0]
for i in range(size):
    lBound[i] = h = max(h, heights[i])

# fill left bounds array
h = heights[size - 1]
for i in reversed(range(size)):
    rBound[i] = h = max(h, heights[i])

# Water stored is minimum of (left bound, right bound - heights)
water = 0
for i in range(size):
    water += min(lBound[i], rBound[i]) - heights[i]

print(water)

# Can be solved by DP
# https://leetcode.com/problems/trapping-rain-water/solution/
