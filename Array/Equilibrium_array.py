# Important : Prefix sum array

# Its prefix sum array is another array prefixSum[] of same size 
# The value of prefixSum[i] is arr[0] + arr[1] + arr[2] … arr[i].

arr = list(map(int,input().split()))

f=0
for i in range(1,len(arr)-1):
    if sum(arr[:i])==sum(arr[i+1:]):
        f=1
        break

print(i) if f==1 else print(-1)    