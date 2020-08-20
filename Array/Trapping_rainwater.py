# Approach : By Maintaining two arrays (DP)

# Find maximum height of bar from the left end upto an index i in the array left_max.
# Find maximum height of bar from the right end upto an index i in the array right_max.

# Iterate over the height array and update ans:
#     Add min(left_max[i],right_max[i]) - height[i] to rain

n = 4
arr = [7, 4, 0, 9]
    
left,right = [0]*n,[0]*n

left[0] = arr[0]
for i in range(1,n):
    left[i]=max(left[i-1], arr[i])
    

right[n-1] = arr[n-1]
for i in range(n-2,-1,-1):
    right[i]=max(right[i+1], arr[i])

print(left,right)

rain = 0
for i in range(0, n):
    rain += min(left[i], right[i]) - arr[i]

print(rain)

# Approach 2 : optimized Version

left, right = 0, n-1
water = 0

max_left = arr[left]
max_right = arr[right]

while left<right:
    if arr[left] <= arr[right]:
        left+=1
        max_left = max(max_left, arr[left])
        water += (max_left-arr[left])

    else:
        right-=1
        max_right = max(max_right, arr[right])
        wate += (max_right-arr[right])

print(water)