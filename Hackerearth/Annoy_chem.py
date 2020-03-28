from math import gcd
m,n,o,p = map(int,input().split())
 
a, b = m//gcd(m,o), n//gcd(n,p)
c = gcd(a,b)
d = (a*b)/c
 
print(int(d*o/m),int(d*p/n),int(d))