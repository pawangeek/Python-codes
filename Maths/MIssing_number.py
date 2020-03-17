# Task : One of the integers is missing in the list from given (1 to N), No Duplicates
# Approach : sum (n*n+1)/2 and subtract array

t = int(input())

while t:
    n = int(input())
    arr = list(map(int,input().split()))
    
    print(((n*(n+1))//2) - sum(arr))
    t-=1