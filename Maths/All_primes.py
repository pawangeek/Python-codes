import math

t = int(input())
d,r=[],t

while t%2==0:
    t = int(t/2)
    d.append(2)

for i in range (3, int(math.sqrt(r))+1,2):

    if t%i==0:
        t=int(t/i)
        d.append(i)
    else:
        continue

print(d)