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
    
        