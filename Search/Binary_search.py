# Complexity : O(n) = O(n/2)+c. Solving it gives O(logn)
# Concept : Get mid of the array. Find element is greater than it or not. and recur in remaining elements

t = int(input())
arr = list(map(int,input().split()))
l = 0

while (l<=len(arr)):
    mid = l+(len(arr)-l)//2

    if arr[mid]==t:
        print(mid)
    
    elif arr[mid]>t:
        r=mid-1
    
    else:
        l=mid+1
        