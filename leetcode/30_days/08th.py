# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291/
# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

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