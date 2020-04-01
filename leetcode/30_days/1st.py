# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

from collections import Counter

nums = list(map(int,input().split()))
p = Counter(nums)
        
for key,value in p.items():
    if value == 1:
        print(key)
        break