# Return minimum and maximum in an array. You program should make minimum number of comparisons.
# Method : Compare in pairs

# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/  
arr = list(map(int,input().split()))
n = len(arr)

# condition for even number
# Select two element in start stating maxmimum as mx and minimum as mn out of two

if (n%2==0):
    mx = max(arr[0],arr[1])
    mn = min(arr[0],arr[1])
    i = 2

# Condition for odd number
# To iter them in same way
else:
    mx = mn = arr[0]
    i = 1

print(mx,mn)

while i < n-1:
    if arr[i]<arr[i+1]:
        mx = max(mx, arr[i+1])
        mn = min(mn, arr[i])

    else:
        mx = max(mx, arr[i])
        mn = min(mn, arr[i+1])

    i+=2

print(mx,mn)