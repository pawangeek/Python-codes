# @Date:   2020-04-27T20:26:04+05:30
# @Last modified time: 2020-04-27T20:59:10+05:30
from heapq import heappop, heappush

n = 18
primes = [2,3,5]

h, heap = set([1]), [1]

while n:
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

    print(h)
    n-=1

print (a)
