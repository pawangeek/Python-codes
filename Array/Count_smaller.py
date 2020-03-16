# Task to calculate the right small elements in array 
# Naive Approach : O(n^2)

t = int(input())

while t:
    p = int(input())
    arr = list(map(int,input().split()))
    k = []
    
    for i in range(p):
        c=0
        for j in range(i+1,p):
            if arr[i]>arr[j]:
                c+=1
            
        k.append(c)
    
    for i in k:
        print(i,end=' ')

    t-=1