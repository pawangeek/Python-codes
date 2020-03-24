# https://practice.geeksforgeeks.org/problems/find-prime-numbers-in-a-range/0

for i in range(int(input())):
    m,n = map(int,input().split())
    
    cnt=0
    for i in range(m,n+1):
        if i == 1:
            continue
        
        f=1
        
        # Simple prime condition ( Dont use sieve here )
        for j in range(2,i//2+1):
            if i%j==0:
                f=0
                break
                
        if (f == 1): 
            print(i, end = " ")
            
    print('')