a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))

while len(a2)>2:

    l = len(a1)
    med1,med2 = (a1[0]+a1[l-1])//2, (a2[0]+a2[l-1])//2

    if med1 == med2:
        print(med1)
        break

    if med1 > med2 and len(a1)>2:
        a1,a2 = a1[0:l//2+1],a2[l//2:l]

    if med1 < med2 and len(a1)>2:
        a1,a2 = a1[l//2:l],a2[0:l//2+1]

if len(a1)==2 and len(a2)==2:
    s = (max(a1[0],a2[0])+min(a1[1],a2[1]))
    print(s/2) 