# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/

# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]
# Direction can be 0 (for left shift) or 1 (for right shift). 
# amount is the amount by which string s is to be shifted.

s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]]

sh = 0

for i in shift:

	# left shift for "0"
    if i[0] == 0:
        sh += i[1]

    # right shift for "1"
    else:
        sh -= i[1]

# it will change negative to positive
sh %= len(s)  
print (s[sh:] + s[:sh])