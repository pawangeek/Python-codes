from heapq import heapify, heappop, heappush

for i in range(int(input())):
    m = int(input())
    arr = list(map(int,input().split()))
    
    heapify(arr)
    tot = 0

    for i in range(m-1):
        x = heappop(arr)
        y = heappop(arr)
    
        z = x+y
        tot+=z

        heappush(arr,z)
        
    print(tot)