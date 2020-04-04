# Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 
# Return how many groups have the largest size.

# https://leetcode.com/contest/biweekly-contest-23/problems/count-largest-group/
# Complexity ; O(n*log(len(n)))
# Since range is 999 which add upto 36 max

n = 13
arr = [0]*37
        
for i in range(1,n+1):
    j,sums = i,0

    # getting sum of digit in range
    while(j > 0): 
        sums += int(j%10) 
        j = int(j/10) 

    # Add it to specific position according to sum ranging (0,36)   
    arr[sums]+=1

# Getting max of array to count          
p = max(arr)

# Getting all with maximum count s    
cnt=0
for i in arr:
    if i==p: cnt+=1
                
print (cnt)