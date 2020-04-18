# https://leetcode.com/contest/biweekly-contest-24/problems/minimum-value-to-get-positive-step-by-step-sum/

# Given an array of integers nums, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

nums = [-3,2,-3,4,2]
a,s = [],0    
        
# Store prefix sum
for i in nums:
    s=s+i
    a.append(s)
        
# Return 1 if minimum of a is 0(positive case) 
# Else return 1-minimum (negative case)
print(1) if min(a)>=0 else print (1-min(a))       