import heapq

for i in range(int(input())):
    a,b=list(map(int,input().split()))
    arr=list(map(int,input().split()))

    k=[]

    for j in range(a):
        heapq.heappush(k,arr[j])

    for j in range(a-1):
        print(-1,end=" ")

    print(k[0],end=" ")

    for j in range(a,b):
        s=k[0]

        if arr[j]>s:
            heapq.heappop(k)
            heapq.heappush(k,arr[j])

        print(k[0],end=" ")
        
    print()