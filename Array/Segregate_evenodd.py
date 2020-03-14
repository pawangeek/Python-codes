# Task is to separate even and odd numbers
# First remove that element from that position and add at last

l = int(input())
arr = list(map(int,input().split()))

for i in arr:
    if i%2==0:       
        arr.remove(i)
        arr.append(i)

print(arr)