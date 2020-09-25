mat =  [[10, 33, 13, 15],
        [22, 21, 4,  1],
        [5 , 0,  2,  3],
        [0 , 6,  14, 2]]

row = len(mat)
col = len(mat[0])

# Declaring maxm for keeping track of maximum gold
maxm = -float('inf')

# Staring from 2nd last row, since last row elements remain as it is
for j in range(row-2,-1,-1):
    for i in range(col-1,-1,-1):

        # Condition for upper most col (we have to choose from >, v directions)
        if i==0:
            mat[i][j] += max(mat[i][j+1], mat[i+1][j+1])
        
        # Condition for lower most col (we have to choose from >, ^ directions)
        elif i==col-1:
            mat[i][j] += max(mat[i][j+1], mat[i-1][j+1])

        # For remaining one (choose from >,^,v directions)
        else:
            mat[i][j] += max(mat[i][j+1], mat[i-1][j+1], mat[i+1][j+1])

        maxm = max(maxm, mat[i][j])

for i in range(4):
    print(mat[i])

print(maxm)