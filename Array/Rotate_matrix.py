lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3

A = [lst[i:i+n] for i in range(0, len(lst), n)]

# Reverse matrix
A = [i[::-1] for i in A]

# Transpose matrix
for i in range(len(A)):
    for j in range(i):
        A[i][j], A[j][i] = A[j][i], A[i][j]
        
for i in range(len(A)):
    print(*(A[i]),end = ' ')