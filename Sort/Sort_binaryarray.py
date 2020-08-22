arr = [1, 0, 0, 0, 1, 0, 1, 1 ]
n = 8

def partition(arr,n):

    pivot = 1
    j = 0

    # Each time we encountered a zero, j is incremented
    # And zero placed before it

    for i in range(n):

        if arr[i]<pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j+=1

    
partition(arr, n)

print(arr)