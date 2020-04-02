# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
# Return the number of sub-arrays of size k and average greater than or equal to threshold.

# Concept : Sum of just new number added and removing the number leave


# Naive Approach : Getting TLE at 68/69 test case
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

cnt=0
for i in range(len(arr)-(k-1)):
    if (sum(arr[i:i+k]))/k >= threshold:
        cnt+=1
        
print(cnt)

# More efficient : Just add new number and subtract last one
cnt=0

# Get sum of a range k prev        
s = (sum(arr[:k]))

# Check if that is greater than threshold      
if s/k>= threshold:
    cnt=1

# Now check every else pair        
for i in range(1,len(arr)-(k-1)):
    s = s-arr[i-1]+arr[i+(k-1)]
            
    if (s/k) >= threshold:
        cnt+=1
        
print (cnt)