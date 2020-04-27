# @Date:   2020-04-27T21:22:27+05:30
# @Last modified time: 2020-04-27T21:27:20+05:30
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
from heapq import heappop, heappush, heapify
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

len1 = len(nums1)
len2 = len(nums2)
result = []

if len1 == 0 or len2 == 0:
    print (result)

# smallest item is guaranteed to be in this subset of combinations
heap = [(nums1[i1] + nums2[0], i1, 0) for i1 in range(len1)]
heapify(heap)

while len(result) < k and len(heap) > 0:

    # this is the next smallest item
    s, i1, i2 = heappop(heap)
    result.append((nums1[i1], nums2[i2]))

    # move pointer i2 to next in the list, and add it to the heap
    i2 += 1
    if i2 < len2:
        nextnum = nums1[i1] + nums2[i2]
        heappush(heap, (nextnum, i1, i2))

print (result)
