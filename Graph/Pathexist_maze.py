from collections import deque

mat = [[1, 1, 1, 0, 0], 
       [0, 0, 1, 0, 1], 
       [1, 1, 1, 1, 1], 
       [0, 0, 1, 1, 0], 
       [1, 0, 1, 1, 1]] 

def shortestmaze(mat, destr, destc):

    path = [(-1,0), (1,0), (0,-1), (0,1)]

    if mat[0][0]==0 or mat[destr][destc]==0:
        return -1

    sour = deque()
    step, flag = 0, 0
    flag = False

    sour.append((0, 0, step))

    while sour:

        row, col, step = sour.popleft()

        if row==destr and col==destc:
            flag = True
            break

        for i, j in path:

            rowx = row+i
            colx = col+j

            # if out of boundaries don't consider
            if rowx<0 or rowx>=len(mat) or colx<0 or colx>=len(mat[0]):
                continue
            
            # If it's zero don't consider
            if mat[rowx][colx]==0:
                continue

            mat[rowx][colx]=0
            sour.append((rowx, colx, step+1))

    return step if flag else -1

print(shortestmaze(mat, 4, 4))