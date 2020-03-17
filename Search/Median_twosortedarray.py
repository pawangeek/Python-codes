a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))

l,a = len(a1),1
print(a1[0],a1[l-1])

while a:
    med1 = (a1[0]+a1[l-1])//2
    med2 = (a2[0]+a2[l-1])//2

    print(med1,med2)

    if med1 == med2:
        print(med1)
        break

    if med1 > med2 and len(a1)>2:
        a1,a2 = a1[0:l//2],a2[l//2:l-1]

    if med1 < med2 and len(a1)>2:
        a1,a2 = a1[l//2:l-1],a2[0:l//2]

    if len(a1)==2 and len(a2)==0:
        print((max(a1[0],a2[0])+min(a1[1],a2[1]))//2)
        break

    print(a1,a2)