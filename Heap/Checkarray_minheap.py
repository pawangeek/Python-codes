def checkmin(A, i):

    if 2*i+2>len(A):
        return True

    left = (A[i] <= A[2*i+1]) and checkmin(A, 2*i+1)
    right = (2*+2 == len(A) or A[i]<= A[2*i+2]) and checkmin(A, 2*i+2)

    return left and right
    # It return true if both are according to constraints
    

