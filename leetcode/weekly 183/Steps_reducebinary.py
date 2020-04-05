# https://leetcode.com/contest/weekly-contest-183/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

# If the current number is even, you have to divide it by 2.
# If the current number is odd, you have to add 1 to it.

s = "1101"

# to convert into decimal
dec,cnt =  int(s,2),0
        
while dec!=1:
            
    # if odd number
    if dec%2==1:
        dec+=1
        cnt+=1
                
    # if even number
    else:
        dec = dec//2
        cnt+=1
            
print (cnt)