# Idea is to use heap to get nth smallest element

from heapq import heappop, heapify

arr = [7, 10, 4, 3, 20, 15]
k, n = 3, 6

heapify(arr)
cnt = 1

for i in range(k):
    
    if cnt==k:
        print(heappop(arr))

    else:
        heappop(arr)

    cnt+=1