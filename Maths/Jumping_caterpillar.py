# Problem statement : Jumping catepillars with no. of caterpillars and jumping factors
# Technique : Sieve of Eratosthenes. Removing all numbers multiples of given no. from range given

t = int(input())

while t:
    m,n = map(int,input().split())
    arr = list(map(int,input().split()))
    d =  []

    for i in arr:

        if i<=m:
            d.append(i)
        
            for j in range(i+i,m+1,i):           
                d.append(j)

    print(d)

    print(m-len(list(set(d)))) 
    t-=1