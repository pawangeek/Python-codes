a = [9,-3,5,-2,-8,-6,1,3]
n = len(a)

def partition(a, start, end):
    pindex = start

    for i in range(start, end):

        if (a[i]<0):
            a[i], a[pindex] = a[pindex], a[i]
            pindex+=1

partition(a, 0, n-1)
print(a)