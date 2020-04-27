# @Date:   2020-04-24T22:09:22+05:30
# @Last modified time: 2020-04-27T12:22:54+05:30

import math
def smallestDivisor(nums, threshold):

    j=1
    while j:

        s=0
        for i in nums:
            s+=int(math.ceil(i/j))
        print(s)

        if s<=threshold:
            return j
        else:
            j+=1

nums = [2,3,5,7,11]
threshold = 11

print(smallestDivisor(nums,threshold))
