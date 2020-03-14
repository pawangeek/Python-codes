l = int(input())
arr = list(map(int,input().split()))

arr.sort(reverse=True)
d=[]

for i in range(int(len(arr)/2)):
    d.append(arr[i])
    d.append(arr[l-i-1])

if l%2==1:
    d.append(arr[i+1])

print(d)