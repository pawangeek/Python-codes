# @Date:   2020-04-27T18:16:28+05:30
# @Last modified time: 2020-04-27T20:14:39+05:30
# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter, OrderedDict
from heapq import nlargest

# Simple nlogk solution
# Just make counter, sort the counter list by most_common or nlargest

nums = [3,4,3,1,3,1,4,1,2,1,2,3]
k = 2

count = Counter(nums)
print (nlargest(k, count.keys(), key=count.get))


# bucket Approach
from itertools import chain

# Create len(nums) bucket
bucket = [[]for _ in nums]

for num,freq in count.items():
    bucket[-freq].append(num)

# Create frequency list
# [[], [], [], [], [], [], [], [], [3, 1], [], [4, 2], []]

# Chain used to convert list of lists to list (Flasttening)
print(list(chain(*bucket)))
