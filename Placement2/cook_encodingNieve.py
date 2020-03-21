t = int(input())
while t!=0:
	nl,l = map(int,input().split())
	nr,r = map(int,input().split())

	count = 0
	for i in range(l,r+1):
		l=[]
		while i!=0:
			r=i%10
			l.append(r)
			i = i//10

		for j in range((len(l)-1),-1,-1):
			if j==(len(l)-1):
				count+=l[j]*(10**j)
			else:
				if l[j]!=l[j+1]:
					count+=l[j]*(10**j)

	print(count%(10**9+7))
	t-=1
