def dfsutil(x, y, k, fill, req):
    
    row, col = len(fill), len(fill[0])

    # If x, y is out of bounds than return
    if x<0 or x>=row or y<0 or y>=col:
        return
    
    # Or that cell is not required one or already changed then return
    if fill[x][y]!=req or fill[x][y]==k:
        return
    
    # Else change that
    fill[x][y] = k
    
    rnbr = [-1, 0, 0, 1]
    cnbr = [0, 1, -1, 0]
    
    # And call dfs for all its adjacant sides
    for dx,dy in zip(rnbr,cnbr):
        dfsutil(x+dx, y+dy, k, fill, req)
        
    return fill
        
fill = [[1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 0, 0], 
        [1, 0, 0, 1, 1, 0, 1, 1], 
        [1, 2, 2, 2, 2, 0, 1, 0], 
        [1, 1, 1, 2, 2, 0, 1, 0], 
        [1, 1, 1, 2, 2, 2, 2, 0], 
        [1, 1, 1, 1, 1, 2, 1, 1], 
        [1, 1, 1, 1, 1, 2, 2, 1]]

x, y, k = 4, 4, 3

# We have to change this cell
req = fill[x][y]  

# Our idea is to use dfs recursively
lst = (dfsutil(x, y, k, fill, req))

for i in range(len(lst)):
    print(lst[i])  