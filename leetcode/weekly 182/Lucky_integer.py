# Find a lucky integer is an integer which has a frequency in the array equal to its value.

# https://leetcode.com/contest/weekly-contest-182/problems/find-lucky-integer-in-an-array/
# Difficulty - very easy

from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        # Get counter of numbers
        y = Counter(arr) 
        c,d=[],-1
        
        # matching occurences with number
        for key, value in y.items(): 
            if key==value:
                c.append(key)
        
        # if none is there return 0 else return biggest one
        return -1 if len(c)==0 else return max(c)