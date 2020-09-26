import math

# Utility fuction to get divisor in O(root(N))
def getdivisors(n) :

    store = set() 
    i = 1
    while i <= math.sqrt(n): 
          
        if (n % i == 0) : 
            if (n//i == i) : 
                store.add(i)
            else :
                store.add(i)  
                store.add(n//i) 
        i = i + 1

    return store

# O(N) for loop over array
# O(root(N)) for finding factorial
# O(1) For loopup from set

for _ in range(int(input())):

    n = int(input())
    arr = list(map(int, input().split()))
    flag = True

    for n,i in enumerate(arr):
        fact = getdivisors(n+1)

        if i in fact:
            continue
        else:
            flag = False
            break

    print("YES") if flag else print("NO")