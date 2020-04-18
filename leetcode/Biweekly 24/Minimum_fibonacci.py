# https://leetcode.com/contest/biweekly-contest-24/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

k = 19
f,i = [0,1,1],3 
        
while True:  
    n = (f[i - 1] + f[i - 2]) 
            
    if n > k: 
        break   

    f.append(n)  
    i += 1
        
c, j = 0, len(f) - 1
        
while k > 0:   
    c += k//f[j]  
    k %= f[j]  
    j -= 1
      
print(c) 