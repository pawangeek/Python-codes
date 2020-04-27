# @Date:   2020-04-27T10:18:32+05:30
# @Last modified time: 2020-04-27T21:35:12+05:30
# https://leetcode.com/problems/super-ugly-number/

primes = [2,3,5]
n = 18

c,lst,g = 1,[1],2
cnt=0

# Simple optimized brute force (168-> 108 checks)
# TLE

while c<n:

    x,i = g,0
    while i<(len(primes)):

        print(x,primes[i])
        cnt+=1

        if x<primes[i]:
            break

        if x%primes[i]==0:
            x = x//primes[i]
        else:
            i+=1

        if x==1:
            break

    if x==1:
        lst.append(g)
        c+=1

    g+=1

# Heap Method
# Ac

from heapq import heappop, heappush

h, heap = set([1]), [1]

while n-1:
    a = heappop(heap)

    # Key points is only those multiples added in this list
    # we get numbers formed by any two in list
    # Append that numbers and than search for formed with two

    for i in primes:
        m = a*i

        # If not present in set
        # Then push that to heap
        if not m in h:
            heappush(heap,m)
            h.add(m)

    n-=1
    print(h)

print(a)
