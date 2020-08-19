# For given array arrange them in max1, min1, max2, min2.... like this

for i in range(int(input())):

    n = int(input())
    arr = list(map(int, input().split()))

    mx, mn = n-1, 0
    elem = arr[n-1]+1

    for i in range(n):

        if i%2==0:
            arr[i] += (arr[mx]%elem) * elem
            mx-=1

        else:
            arr[i] += (arr[mn]%elem) * elem
            mn+=1

    print ([arr[i]/=elem for i in range(n)])