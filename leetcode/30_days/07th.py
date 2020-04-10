# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/
# Given an integer array arr, count element x such that x + 1 is also in arr.

arr = [1,1,3,3,5,5,7,7]
s,c = set(arr),0
        
for i in arr:
    if (i+1) in s:
        c+=1
        
print (c)