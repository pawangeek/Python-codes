# https://leetcode.com/contest/weekly-contest-183/problems/minimum-subsequence-in-non-increasing-order/
# obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 

nums = [4,3,10,9,8]
# O/P should be [10,9] since sum of [8,4,3] is smaller

nums.sort(reverse = True)
op = []

# Simple approach is just append in new array and pop from original
# Tll we get greater sum        
while sum(op)<=sum(nums):
    op.append(nums[0])
    nums.pop(0)
            
print (op)