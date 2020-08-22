# Approach 1 : By using div operator

for i in range(int(input())):
    
    n, mul = int(input()), 1
    arr = list(map(int, input().split()))
    
    for i in range(n):
        mul *= arr[i]
        
    print(*([(mul//arr[i]) for i in range(n)]))


# Approach 2 : Using prefix suffix array

for i in range(int(input())):
    
    n, temp = int(input()), 1
    arr = list(map(int, input().split()))
    
    prod = [1]*n
    
    for i in range(n):
        prod[i] = temp
        temp*=arr[i]
        
    temp = 1
    
    for i in range(n-1,-1,-1):
        prod[i] *= temp
        temp*=arr[i]
        
    print(*(prod))
        
        

