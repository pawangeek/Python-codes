# Task : to find repeating and misssing number in given array:
# Inefficient : sort take O(nlogn) time itself

t = int(input())

while t:
    p = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    c,d,g,f = 0,0,0,0
    
    if arr[0]!=1:
        d,g = 1,1
    
    for i in range(p):
        
        if arr[i+1]==arr[i] and f == 0:
            c,f = arr[i],1
        
        elif arr[i+1]!=(arr[i]+1) and g == 0:
            d,g = arr[i]+1,1
            
        if (c!=0 and d!=0):
            break
  
    print(c,d) 
    t-=1    