def minDist(arr, n, x, y):
    
    if x not in arr or y not in arr:
        return -1
        
    dist = -1
    min_dist = float('inf')
    
    for i in range(n):
        
        if arr[i]==x or arr[i]==y:
            
            if dist!=-1 and arr[i]!=arr[dist]:
                min_dist = min(min_dist, i-dist)
                
            dist = i
            
    return min_dist