# Task to count all zeros among given array of zero and one. Expected complexity = log(N)

t = int(input())
while t:
    
    p=int(input())
    
    arr = list(map(int,input().split()))
    print(p-sum(arr))
    
    t-=1