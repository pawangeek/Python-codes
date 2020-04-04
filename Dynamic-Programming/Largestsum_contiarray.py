# We have to find largest sum of contiguous subarray
arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]

max_ending = 0
max_so_far = -1*float("inf")

for i in range(len(arr)):

    max_ending = max_ending + arr[i] 

    # If sum is growing then store it in max_so_far
    if (max_so_far < max_ending):
        max_so_far = max_ending

    # If sum upto position is less then 0 then reset the sum
    if max_ending < 0: 
        max_ending = 0  

print(max_so_far)