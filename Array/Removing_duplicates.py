# To remove all duplicates from list preserving the order
# We cant use set here since it don't preserve the order

# Approach : We use Ordereddict. fromkeys
# Fromkeys() : fromkeys() method returns a new dictionary with the given sequence of elements as the keys of the dictionary.

# For example list is [a,b,c,d] then it creates a list as {a:None, b: None, c: None, d: None} 
# And keys are unique that's why they dont repeat

from collections import OrderedDict
t = int(input())

while t:
    p = input()
    print(''.join(OrderedDict.fromkeys(p)))

    t-=1