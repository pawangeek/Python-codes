# Task : To find element with count = 1 in array
# Approach 1 : To create counter dict and than select key with value 1

from collections import Counter
t = int(input())

while t:
    p = int(input())
    arr = list(map(int,input().split()))
    
    arr = Counter(arr)
    print(list(arr.keys())[list(arr.values()).index(1)])

    t-=1

# Approach 2 : To double each element and subtract sum(array) from 2*(doubling)

t = int(input())

while t:
    p = int(input())
    arr = list(map(int,input().split()))
    s=0
    
    for i in range(0,p,2):
        s=s+arr[i]
    
    print((2*s)-sum(arr))
    t-=1