from math import gcd
from itertools import combinations
t = int(input())

d,gc=[],0

for i in range(1,t+1):
    d.append(i)

f = list(combinations(range(1,t+1),2))
print(f)

for i in f:
    gc = gc+gcd(i[0],i[1])

print(gc)