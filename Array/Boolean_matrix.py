# Approach 1: Using additional space

for i in range(int(input())):
    
    n, m = map(int, input().split())
    
    arr = [0]*n
    for i in range(n):
        arr[i] = list(map(int, input().split()))
        
    rows, cols = set(), set()
    
    for i in range(n):
        for j in range(m):
            
            if arr[i][j]==1:
                rows.add(i)
                cols.add(j)
    
    print(rows,cols)
                
    for i in range(n):
        for j in range(m):
            
            if i in rows or j in cols:
                arr[i][j]=1
                
    for i in range(n):
        print(*(arr[i]))
        
        