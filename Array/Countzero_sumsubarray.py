arr =  [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
n = len(arr)

# Same logic for question : No. of subarrays with equal 0s and 1s
# Just change all 0s to -1

# Approach 1 : Brute Force
cntr = 0
cnt = 0
for i in range(len(arr)):
    sum1 = 0

    for j in range(i, len(arr)):
        cntr+=1
        
        sum1+=arr[j]
        if sum1==0:
            cnt+=1

print(cnt,cntr)

# Approach 2 : Hashing
dict = {}

# Sum tracker
sum1 = 0
cnt = 0 

for i in range(n):

    sum1 += arr[i]

    if sum1==0:
        cnt+=1

    if sum1 in dict:
        cnt+=dict[sum1]
        dict[sum1]+=1

    else:
        dict[sum1] = 1

print(dict)
print(cnt)
