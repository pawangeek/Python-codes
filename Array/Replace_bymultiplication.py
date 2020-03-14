# we have to replace element by multiplcation of prev and next element
# i) First by first and second
# ii) last by last and second last


l = int(input())
arr = list(map(int,input().split()))
d=[]

for i in range(1,l):

    if i==1:
        a = arr[0]*arr[i]
        d.append(a)
        
    if i>=1 and i<l-1:
        a = arr[i-1]*arr[i+1]
        d.append(a)
    
    else:
        a = arr[i-1]*arr[i]
        d.append(a)

print(d)