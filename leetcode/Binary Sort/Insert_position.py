# @Date:   2020-04-24T20:52:32+05:30
# @Last modified time: 2020-04-27T12:15:26+05:30
def binary(nums,target):

    l, r = 0, len(nums)
    while l<r:

        mid = l+r//2

        # If got target element return position
        if nums[mid]==target:   #3
            return mid

        # if target is bigger than mid
        # Reduce search space to right half
        elif nums[mid]<target:  #1
            l=mid+1

        # Else to left half
        else:                   #2
            r=mid

    return(r)

# Iter 1 : l = 0, r = 6, mid = 2
# cond 1 : target = 5, nums(mid) = 4
# Iter 2 : l = 3, r = 6, mid = 3
# cond 2 : target = 5, nums(mid) = 6
# Iter 3 : l = 3, r = 3
nums = [1,2,4,6,9]
target = 5
print(binary(nums,target))
