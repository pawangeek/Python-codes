# Better Approach

from heapq import heapify, heappop

for i in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    heapify(arr)
    l1, l2 = [], []
    
    for i in range(n//2):
        l1.append(heappop(arr))
        l2.append(heappop(arr))
    
    if n%2==1:
        l1.append(heappop(arr))
        
    l1 = [str(i) for i in l1]
    l2 = [str(i) for i in l2]
    
    print(int(''.join(l1))+int(''.join(l2)))
    
# Efficient Approach
arr = [6, 8, 4, 5, 2, 3 ] 

mx = 10
freq = [0]*mx
k = 0

for i in range(len(arr)):
    freq[arr[i]] += 1

for i in range(mx):

    for j in range(freq[i]):
        arr[k] = i
        k += 1

l1,l2 = 0,0

for i in range(len(arr)):
    if i%2==0:
        l1 = l1*10+arr[i]
    else:
        l2 = l2*10+arr[i]

print(l1+l2)
