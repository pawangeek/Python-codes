a = [9, -3, 5, -2, -8, -6, 1, 3]
n = len(a)

def partition(a, n):

    j = 0
    pivot = 0

    for i in range(n):

        if a[i]<pivot:
            a[i], a[j] = a[j], a[i]
            j+=1

    return j

def rearrange(a, n):

    p = partition(a, n)

    i = 0
    while p<n and i<p:
        a[i],a[p] = a[p],a[i]
        i+=2
        p+=1

    return a

print(rearrange(a,n))
