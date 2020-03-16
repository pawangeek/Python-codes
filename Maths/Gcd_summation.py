from math import gcd
from itertools import combinations
t = int(input())

f,gc = list(combinations(range(1,t+1),2)),0

for i in f:
    gc = gc+gcd(i[0],i[1])

print(gc)