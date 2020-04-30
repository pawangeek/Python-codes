# @Date:   2020-04-30T17:20:23+05:30
# @Last modified time: 2020-04-30T17:29:52+05:30

# https://leetcode.com/problems/largest-number/
# Given a list of non negative integers, arrange them such that they form the largest number.

# Approach (Libarary Fuction)

from functools import cmp_to_key as cmp
nums = [3,30,34,5,9]

# convert all elements of the list from int to string
nums = map(str, nums)

# we define a function that compares two string (a,b)
# we consider a bigger than b if a+b>b+a
# for example : (a="2",b="11") a is bigger than b because "211" >"112"
comp = lambda a,b:1 if a+b < b+a else -1 if a+b > b+a else 0

# sort the list descendingly using the comparing function we defined
# for example sorting this list ["2","11","13"] produce ["2","13","11"]
# Then concatenate
biggest = ''.join(sorted(nums, key=cmp(comp)))

# convert to int to remove leading zeroes
print (str(int(biggest)))

# Approach Custom operator
# Detailed : https://leetcode.com/problems/largest-number/solution/

def __lt__(x, y):
    return x+y > y+x
