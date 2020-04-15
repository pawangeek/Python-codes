# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3300/
# Product of Array Except Self

# Given an array nums of n integers where n > 1
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

nums=[1,2,3,4]        

numsLen = len(nums)
productWithoutSelf = [1] * numsLen
        
# productWithoutSelf[i] as product of elements to the left of nums[i].
for i in range(1, numsLen):
    productWithoutSelf[i] = productWithoutSelf[i - 1] * nums[i - 1]
        
# productWithoutSelf[i] multiply product of elements to the right of nums[i].
rightProduct = 1
for i in range(numsLen - 1, -1, -1):
    productWithoutSelf[i] *= rightProduct
    rightProduct = rightProduct * nums[i]
            
print(productWithoutSelf)