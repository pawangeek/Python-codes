# @Date:   2020-04-26T23:44:16+05:30
# @Last modified time: 2020-04-26T23:53:09+05:30
# https://leetcode.com/problems/jump-game/

nums = [2,3,1,1,4]
m = 0

for i, n in enumerate(nums):
    if i>m:
         print(False)

    # Cover till (i+n) and put to m
    else:
        m = max(m,i+n)

print(True)
