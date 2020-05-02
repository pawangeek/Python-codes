# @Date:   2020-05-02T16:49:41+05:30
# @Last modified time: 2020-05-02T16:52:55+05:30

def search(nums, target):

    l = 0
    r = len(nums)-1

    while l<=r:
        mid = (l+r)//2

        # if we got that target
        if nums[mid]==target:
            return mid

        # if current element is greater than target
        elif nums[mid]>target:
            r = mid-1

        # if current element is smaller than target
        else:
            l = mid+1

    # If not found return -1
    return -1

nums = [-1,0,3,5,9,12]
target = 9

print(search(nums,target))
