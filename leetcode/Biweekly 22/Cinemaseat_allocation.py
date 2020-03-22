# Return the maximum number of four-person families you can allocate on the cinema seats.
# https://leetcode.com/contest/biweekly-contest-22/problems/cinema-seat-allocation/

# Difficulty : Medium
# Concept : Hashmap (Dictionary)

from collections import defaultdict

n = 3
rev = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]

d = defaultdict(list)
print(d)

f1, f2, f3, res = [2,3,4,5], [4,5,6,7], [6,7,8,9], 0