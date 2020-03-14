# Task is to rotate array like [1,2,3,4,5] to [5,4,3,2,1]
# concept is to store each one in temp and replace both positions

l = int(input())
arr = list(map(int, input().split()))

for i in range(int(l/2)):
    temp = arr[i]
    arr[i]=arr[l-i-1]
    arr[l-i-1]=temp

print(arr)