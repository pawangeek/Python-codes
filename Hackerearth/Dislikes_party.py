# https://www.hackerearth.com/problem/algorithm/dislikes-and-party-567b9605/

t = int(input())
 
arr,p = [],[]
for i in range(10):
    arr.append(list(map(int,input().split())))
 
# Make p is a list of list getting every possibity of hanshakes
# Eg. [[7, 3], [7, 11], [7, 4], [7, 5], [7, 6]]
for i in arr:
    for j in range(1,10):
        p.append([i[0],i[j]])

# Total handshakes : t*(t-1))//2

# Removing those sublists which are repeated from p
# And remove them from total handshakes

print((t*(t-1))//2 - len(list(set(tuple(item) for item in map(sorted, p)))))