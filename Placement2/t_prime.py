def sieve(n,prime):
	p = 2

	while p**2<=n:
		if prime[p]:
			for i in range(p*2,n+1,p):
				prime[i]=False
		p+=1

n = int(input())
x = list(map(int,input().split()))

s = [True]*(10**6+1)

sieve(10**6,s)

for i in x:
	if i<4:
		print("NO")
		continue
	elif int(i**0.5)**2 != i:
		print('NO')
		continue

	if s[int(i**0.5)]:
		print("YES")
	else:
		print("NO")