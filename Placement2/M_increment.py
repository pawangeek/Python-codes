m,n = map(int,input().split())
arr = [0]*m

for i in range(n):
	p,q,r = map(int,input().split())

	for i in range(p,q+1):
		arr[i] = arr[i]+r

print(max(arr))