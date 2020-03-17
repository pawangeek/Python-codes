# Complexity : log(N)
t = int(input())

for i in range(t):
    s = int(input())
    a = list(map(int,input().split()))
    e = int(input())

    low,high,flag = 0,s-1,0

    while (low<=high):

        mid = (low+high)//2

        if a[mid]==e:
            flag=1
            print(mid)
            break
        
        if a[mid]>a[low]:
            if (e>=a[low] and e<a[mid]):
                high = mid-1
            else:
                low = mid+1
        
        else:
            if (e<=a[high] and e>a[mid]):
                low = mid+1
            else:
                high = mid-1

    if flag==0:
        print(-1)