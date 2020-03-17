# Problem statement : No Reapeated element in array. Find rotation in sorted array
# Complexity : O(log(n)) (using binary search)

t = int(input())

while t:
    p = int(input())
    arr = list(map(int,input().split()))
    
    low,high=0,p-1
    while low<=high:
        
        if arr[low]<=arr[high]:
            print(low)
            break
        
        mid = (low+high)//2
        next = (mid+1)%p
        prev = (mid+p-1)%p
        
        if arr[mid]<=arr[next] and arr[mid]>=arr[prev]:
            print(mid-1)
            break
            
        if arr[mid]>=arr[low]:
            low=mid+1
        
        if arr[mid]<=arr[high]:
            high=mid-1
        
    t-=1
        