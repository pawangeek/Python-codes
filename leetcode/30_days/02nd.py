# Happy Number

# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/
# Write an algorithm to determine if a number is "happy".

# Imp : Just put the condition in return/print for True/False

n=19

seen = set()
while n not in seen:
    seen.add(n)
    n = sum(int(x) **2 for x in str(n))

print (n == 1)