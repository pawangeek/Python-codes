# if x is even then x = x / 2
# if x is odd then x = 3 * x + 1

# https://leetcode.com/contest/biweekly-contest-22/problems/sort-integers-by-the-power-value/
# Concept : Number Theory
# Difficulty : Easy

lo,hi,k = map(int,input().split())

arr,p=[],[]
    
for i in range(lo,hi+1):
    p.append(i)
        
    t = 0
    while i!=1:
        if i%2==0:
            i,t = i/2,t+1
        else:
            i,t = (3*i)+1,t+1
            
        arr.append(t)
    
    z = [x for _,x in sorted(zip(arr,p))] # Getting desired indexed element
    print(z[k-1])   