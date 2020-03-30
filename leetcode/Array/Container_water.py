# https://leetcode.com/problems/container-with-most-water/
# We have to find maximum water a array can hold ( height * lenght )

arr = list(map(int,input().split()))
l = len(arr)

i,j = 0,l-1
max_area = 0

while i<j:

    # area = height * lenght
    area = min(arr[i],arr[j])*(j-i)

    # Get maximum area (prev stored and current)
    max_area = max(max_area, area)

    # Try to remove minimum minimum one
    if arr[i]>arr[j]:
        j+=1
    else:
        i+=1

# It's not matter if both are equal since it may leads to situation
# Either (i,j-1) or (i+1,j) equal or small in that case
    