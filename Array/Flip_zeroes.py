arr = [0,1,0,0,1,1,0]

curr_max = 0
max_diff = 0
zero_count = 0

for i in range(len(arr)):

    if arr[i]==0:
        zero_count+=1

    if arr[i]==1:
        val=1
    else:
        val=-1

    curr_max = max(val, curr_max+val)
    max_diff = max(max_diff, curr_max)

maxdiff = max(0,max_diff)
print(zero_count)
print(zero_count+max_diff)
