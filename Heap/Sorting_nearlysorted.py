# https://www.geeksforgeeks.org/nearly-sorted-algorithm/
# Important Question

from heapq import heapify, heappop, heappush

t = int(input())
arr = list(map(int,input().split()))

heap = arr[:t + 1] 
heapify(heap)

print(list(heap))
p =[]

cnt=0
for i in range(t+1,len(arr)):
    print(arr)
    arr[cnt] = heappop(heap)
    heappush(heap, arr[i])
    cnt+=1

print(list(heap),cnt)
print(arr)

while heap:
    arr[cnt]=heappop(heap)
    cnt+=1

print(arr)
