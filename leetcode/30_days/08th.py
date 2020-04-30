# @Date:   2020-04-10T11:28:59+05:30
# @Last modified time: 2020-04-30T17:10:47+05:30

# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291/
# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Build String (stack approach)
S = "ab#c"
T = "ad#c"

s = []
t = []

for c in S:
	if c == '#':
		if s != []:
			s.pop()
		else:
			s.append(c)
for c in T:
    if c == '#':
		if t != []:
			t.pop()
		else:
			t.append(c)

return s == t

# Two pointers (approach)

# If instead we iterate through the string in reverse, then we will know how many backspace characters we have seen
# therefore whether the result includes our character.

# Iterate through the string in reverse. If we see a backspace character, the next non-backspace character is skipped.
# If a character isn't skipped, it is part of the final answer.

def F(S):
    skip = 0
    for x in reversed(S):
        if x == '#':
            skip += 1
        elif skip:
            skip -= 1
        else:
            yield x

print (all(x == y for x, y in itertools.izip_longest(F(S), F(T))))

# Time Complexity: O(M + N), where M, NM,N are the lengths of S and T respectively.
# Space Complexity: O(1).
