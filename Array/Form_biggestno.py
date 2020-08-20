# Naive Approach

# Approach one: using permutations
from itertools import permutations

lst = int(input())
arr = list(map(int,input().split()))

print("".join(map(str,max(list(permutations(arr,lst))))))

# Approach two: using custom operator
from functools import cmp_to_key

nums = [11,2,13]
nums = map(str, nums)

comp = lambda a,b : 1 if a+b<b+a else -1 if a+b>b+a else 0

biggest = ''.join(sorted(nums, key=cmp_to_key(comp)))
print(str(int(biggest)))

# Approach three: using extended form
arr = [1, 34, 3, 98, 9, 76, 45, 4, 12, 121]
extval, ans = [],""

len = len(str(max(arr)+1))

for i in arr:
    s = str(i)*len
    extval.append((s[:len],str(i)))

extval.sort(reverse=True)

print(''.join([i[1] for i in extval]))
