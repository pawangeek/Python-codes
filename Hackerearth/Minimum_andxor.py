for _ in range(int(input())):
    t = int(input())
    arr = list(map(int,input().split()))
 
    arr.sort()
    q, a = 10**18, 0
 
    for i in range(t-1):
        a = (arr[i] and arr[i+1])^(arr[i] or arr[i+1])
        q = min(a,q)
 
    print(q)