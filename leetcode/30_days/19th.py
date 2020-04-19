# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3304/
nums = [4,5,6,7,0,1,2]
target = 0

lo, hi = 0, len(nums) - 1

while lo <= hi:
    mid = (lo+hi) // 2
    if nums[mid] == target:
        print (mid)
           
    if nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
        hi = mid - 1
                
    else:
        lo = mid + 1

print (-1)