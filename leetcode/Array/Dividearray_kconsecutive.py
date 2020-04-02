# Divide Array in Sets of K Consecutive Numbers
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

# Given an array of integers nums and a positive integer k, 
# find whether it's possible to divide this array into sets of k consecutive numbers

# Important : sorted(dict) and sorted(dict.key()) gives the same result

from collections import Counter

nums = [3,2,1,2,3,4,3,4,5,9,10,11]
k=4
       
count = Counter(nums)
# Counter({3: 3, 2: 2, 4: 2, 1: 1, 5: 1, 9: 1, 10: 1, 11: 1})

keys = sorted(count)
# [1, 2, 3, 4, 5, 9, 10, 11]

for n in keys:                  # Iterating keys
    if count[n]>0:              # Get to know which first number has count>0 i.e. Here it's 1
        minus = count[n]        # Get values of that key. i.e 1 for 1
                
        for i in range(n,n+k):  # Checking in range 1 to 1+k(1+4=5) i.e. 1,2,3,4
            if count[i]<minus:  # if count of them are less then that of 1 i.e. if 1 has 1 and 2 has 0
                print (False)   # Print False
                break
                    
            count[i]-=minus     # If not then subtract those counts from all 2,3,4
        
print (True)                    # If all of the loop run successfully print True
        