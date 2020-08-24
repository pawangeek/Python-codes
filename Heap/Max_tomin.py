
def convert(arr):

    # call heapify from last node
    i = (len(arr)-2)//2

    while i>=0:
        heapify(arr, i , len(arr))
        i-=1

def heapify(A, i , size):

    left = 2*i+1
    right = 2*i+2

    # if left child is smaller, replace that with parest
    if left<size and A[left]<A[i]:
        smallest = left
    
    # if right child is smaller, replace that with parent
    if right<size and A[right]<A[i]:
        smallest = right

    # If smaller value than swap with the child else done
    if smallest!=i:

        A[i], A[smallest] = A[smallest], A[i]
        heapify(A, smallest, size)

    
