a,b = map(int,input().split())
c = int(input())

if c>min(a,b):
    print(-1)

else:
    d=1
    for i in range(2,min(a,b)):
        if (a%i==0 and b%i==0):
            d+=1

            if d==c:
                d=i
                break
        
        if (d==1 and i==(min(a,b)-1)):
            d=-1
    print(d)