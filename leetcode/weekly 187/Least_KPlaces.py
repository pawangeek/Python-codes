# @Date:   2020-05-03T21:24:44+05:30
# @Last modified time: 2020-05-03T21:28:04+05:30

# https://leetcode.com/contest/weekly-contest-187/problems/check-if-all-1s-are-at-least-length-k-places-away/
# Check If All 1's Are at Least Length K Places Away

nums = [1,0,0,0,1,0,0,1]
k = 2

import sys

if(k==0):
    print(True)

initial = -sys.maxsize- 1
for i in range(len(nums)):
    if(nums[i]==1):

        if(initial!=(-sys.maxsize- 1) and i-initial <= k):
             print(False)
        else:
            initial = i

print(True)
