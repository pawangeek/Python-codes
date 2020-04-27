# @Date:   2020-04-27T10:36:10+05:30
# @Last modified time: 2020-04-27T12:02:57+05:30
# https://leetcode.com/problems/search-in-rotated-sorted-array/

nums = [4,5,6,7,0,1,2]
target = 0

# setting left and right
l = 0
r = len(nums)-1
ans = -1

# Iter 1: l=0, r=6, mid=3
# Cond 2(b), nums[l]=4, nums[mid]=7, target=0

# Iter 2: l=4, r=6, mid=5
# Cond 2(a), nums[l]=0, nums[mid]=1, target=0

# Iter 3: l=4, r=4, mid=4
# Cond 1, break

while l <= r:
    mid = (l+r)//2

    # Condition if we get target as mid
    if nums[mid] == target:                 # cond 1
        ans = mid
        break;

    # if left is less than mid element
    # Means start at right
    if nums[l] <= nums[mid]:                # cond 2

        # If target lies between them then remove all right ones
        if nums[l] <= target < nums[mid]:   # cond 2a
            r = mid - 1

        # If target not lies remove left ones
        else:                               # cond 2b
            l = mid + 1

    # If right is less than mid element
    # Start at left of mid
    else:                                   # cond 3

        # If target lies between them then remove all lefts
        if nums[mid] < target <= nums[r]:   # cond 3a
            l = mid + 1

        #
        else:                               # cond 3b
            r = mid - 1
print(ans)
