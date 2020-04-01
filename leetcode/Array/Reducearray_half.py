# https://leetcode.com/problems/reduce-array-size-to-the-half/

# Important : (i) Sort dictionary by values (most_common)
#             (ii) Use Ordereddict to convert it into dict again (Since it remember order)

from collections import Counter, OrderedDict
import math

arr = [3,3,3,3,5,5,5,2,2,7]

# Getting counter of each number
dct2 = Counter(arr)
		
# Sorting our hashmap occurding to values
dct = OrderedDict(dct2.most_common())
		
# Getting half and one more than half in even and odd resp.
l = int(math.ceil(len(arr)/2))
        
        
p,c = 0,[]
        
# Adding to p till we get equal, greater then l
for key,value in dct.items():
    p = p+value
    c.append(key)
            
    if p>=l:
        print(len(c)) 
        break    