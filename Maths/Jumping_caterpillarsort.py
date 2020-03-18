t = int(input())

while t:
    m,n = map(int,input().split())
    d = list(map(int,input().split()))
    l = list(range(1,m+1))

    for i in sorted(set(d)):
        for j in sorted(l):
            if (j%i==0):
                l.remove(j)

    print(len(l)) 
    t-=1