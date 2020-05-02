# @Date:   2020-05-01T09:27:31+05:30
# @Last modified time: 2020-05-02T16:53:35+05:30

# i) Divide matrix of size N into N/2 and N/2
# ii) Calculate values recusively

#   a | b      e | f        ae + bg | af + bh
#   --|---  x ---|---  =    --------|---------
#   c | d      g | h        ce + dg | cf + dh

# But in above method we have to do 8 multiplication
# T(N) = 8T(N/2) + O(N^2)

import sys
sys.setrecursionlimit(300)

import numpy as np

def split(matrix):

    row, col = matrix.shape
    row2, col2 = row//2, col//2

    a = matrix[:row2, :col2]
    b = matrix[:row2, col2:]
    c = matrix[row2:, :col2]
    d = matrix[row2:, col2:]

    return a,b,c,d

def strassen(x,y):

    # Base case when size is one
    if len==1:
        return x*y

    # Splitting the matrices into quadrants.
    # This will be done recursively untill the base case is reached.
    a,b,c,d = split(x)
    e,f,g,h = split(y)

    p1 = strassen(a, f-h)
    p2 = strassen(a+b, h)
    p3 = strassen(c+d, e)
    p4 = strassen(d, g-e)
    p5 = strassen(a+d, e+h)
    p6 = strassen(b-d, g+h)
    p7 = strassen(a-c, e+f)

    c1 = p5+p4-p2+p6
    c2 = p1+p2
    c3 = p3+p4
    c4 = p1+p5-p3-p7

    l1 = np.hstack((c1,c2))
    l2 = np.hstack((c3,c4))

    print(l1,l2)

    return np.vstack((l1,l2))

m1 = np.matrix([[1, 3], [7, 5]])
m2 = np.matrix([[6, 8], [4, 2]])

print(strassen(m1,m2))
