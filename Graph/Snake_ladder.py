def BFS(d):
    q=[[1,0]]
    
    while q:
        a = q.pop(0)
        pos, throw = a[0], a[1]
        
        # if vertex is detination node, we're done
        if pos == 30:
            return throw
        
        i = pos+1
        while i<31 and i<= pos+6:
            
            # means there is snake or ladder at that position
            # we append reaching one to that position
            if i in d:
                q.append([d[i],throw+1])
            else:
                q.append([i,throw+1])
            
            # otherwise we need to move one step
            i+=1
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    
    d = {}
    for i in range(0,2*n,2):
        d[arr[i]] = arr[i+1]
    
    print(BFS(d))