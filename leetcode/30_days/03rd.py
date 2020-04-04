# Maximum subarray (Dp Problem)

# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/
# Given an integer array nums, find the contiguous subarray
# which has the largest sum and return its sum.

nums = [-2,1,-3,4,-1,2,1,-5,4]

max_ending = 0
max_so_far = -1*float("inf")

for i in range(len(nums)):

    max_ending = max_ending + nums[i] 
    
    if (max_so_far < max_ending):
        max_so_far = max_ending

    # If sum upto position is less then 0 then reset the sum
    if max_ending < 0: 
        max_ending = 0 
                
print (max_so_far)