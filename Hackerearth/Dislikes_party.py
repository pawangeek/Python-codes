t = int(input())
 
arr,p = [],[]
for i in range(10):
    arr.append(list(map(int,input().split())))
 
for i in arr:
    for j in range(1,10):
        p.append([i[0],i[j]])
 
print((t*(t-1))//2 - len(list(set(tuple(item) for item in map(sorted, p)))))