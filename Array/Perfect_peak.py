A = [5,1,4,3,6,8,10,7,9]
mx, mn = [A[0]], [A[-1]]
        
for i in range(1,len(A)):
    mx.append(max(mx[i-1], A[i]))

for i in range(len(A)-2,-1,-1):
    mn.append(min(mn[len(A)-2-(i)], A[i]))

print(0) if set(mx[1:len(A)-1]).intersection(set(mn[1:len(A)-1])) == set() else print(1)