# Divide Array in Sets of K Consecutive Numbers
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

# Important : sorted(dict) and sorted(dict.key()) gives the same result

from collections import Counter

nums = [3,2,1,2,3,4,3,4,5,9,10,11]
k=4
       
count = Counter(nums)
# Counter({3: 3, 2: 2, 4: 2, 1: 1, 5: 1, 9: 1, 10: 1, 11: 1})

keys = sorted(count)
# [1, 2, 3, 4, 5, 9, 10, 11]

for n in keys:
    if count[n]>0:
        minus = count[n]
                
        for i in range(n,n+k):
            if count[i]<minus:
                print (False)
                    
            count[i]-=minus
        
        print(count)
        print (True)
        break
        