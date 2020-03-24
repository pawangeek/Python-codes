# Find the minimum possible sum of two numbers formed from digits of the array.
# https://practice.geeksforgeeks.org/problems/min-sum-formed-by-digits/0

# Aprroach : Sort : O(nlogn) and alternate listing : O(n)

for _ in range(int(input())):
    p = int(input())
    arr = list(map(int,input().split()))
    
    arr.sort()
    q,r=[],[]
    
    for i in range(p):
       q.append(arr[i]) if i%2==0 else r.append(arr[i])
            
    q = int("".join(map(str, q)))
    r = int("".join(map(str, r)))
    
    print(r+q)

# Another method in O(n)
# https://www.geeksforgeeks.org/minimum-sum-of-two-numbers-formed-from-digits-of-an-array-in-on/

