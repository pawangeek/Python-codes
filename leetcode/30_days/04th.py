# Move Zeroes

# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Have to do it inplace

nums = [0,1,0,3,12]

for i in range(len(nums)):
    if nums[i]==0:
        nums.remove(0)
        nums.append(0)

print(nums)