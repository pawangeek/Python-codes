# @Date:   2020-04-24T20:10:26+05:30
# @Last modified time: 2020-04-27T12:05:54+05:30

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Usually in a regular BS function, you would return either True, or the target once you find it
# And we break the while loop

# In these two function (searchLeft) and (searchRight)
# we don't terminate the loop, instead, we keep updating
# the target and the left (or right) index

def get_start(nums,target):

    targetIndex = -1
    l, r = 0, len(nums)-1

    while l <= r:

        mid = (l+r)//2
        if nums[mid] == target:     # condition 1
            targetIndex = mid
            r = mid - 1

        elif nums[mid] < target:    # condition 2
            l = mid+1

        else:                       # condition 3
            r = mid-1

    return targetIndex

# For [5,7,7,8,8,10]

# Iter 1 : l = 0, r = 5 so mid = 2 (l+r//2)
#       condition 2 : nums(mid) = 7, target = 8
# Iter 2 : l = 3, r = 5 so mid = 4
#       condition 1 : nums(mid) = 8, target = 8
# Iter 3 : l = 3, r = 3 so mid = 3
#       condition 1 : nums(mid) = 8, target = 8

def get_end(nums,target):

    targetIndex = -1
    l, r = 0, len(nums)-1

    while l <= r:

        mid = (l+r)//2
        if nums[mid] == target:
            targetIndex = mid
            l = mid + 1

        elif target < nums[mid]:
             r = mid-1

        else:
            l = mid+1

    return targetIndex

return [-1,-1] if get_start(nums,target)==(-1) else [get_start(nums,target), get_end(nums,target)]
