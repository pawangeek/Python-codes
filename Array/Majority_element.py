arr = [0,0,0,1,1,1,2,0,0]

# Approach 1: Inbuilt counter (two pass)

from collections import Counter

n = len(arr)
arr = Counter(arr)
flag = -1

for k,v in arr.items():
    if v>(n//2):
        flag = k

print(flag)

# Approach 2: Creating Counter (one pass)

dict = {}

for i in range(n):

    if arr[i] not in dict:
        dict[arr[i]] = 1

    if dict[i]>len(arr)//2:
        flag = k

    else:
        dict[arr[i]] += 1

# Approach 3: Boyer Moore Voting

cnt, cond = 0, 0

for num in arr:

    if num==cond:
        cnt+=1
    elif cnt == 0:
        cond = num
        cnt = 1
    else:
        cnt -= 1
    