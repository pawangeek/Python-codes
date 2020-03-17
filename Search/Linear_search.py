# Time complexity : O(n)

t = int(input())
arr = list(map(int,input().split()))

g=-1
for i in range(len(arr)):
    if arr[i]==t:
        g = i
        print(g)
        break
