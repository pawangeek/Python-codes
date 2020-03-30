# Given an array of integers, return indices of the two numbers such that they add up to a specific target
# https://leetcode.com/problems/two-sum/

# Using Hashmap space O(n)
#               Time O(n)

arr = list(map(int,input().split()))
target =int(input())

h={}

# Enumerator is used as generator it adds a counter to an iterable
for n,i in enumerate(arr):
    remain = target - i

    # If pair not in dict, append given i as key and n as value 
    if remain not in h:
        h[i]=n

    # If present in it, print both
    else:
        print([h[remain],n])

print(h)

#[2, 7, 11, 15]