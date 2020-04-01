# https://leetcode.com/problems/check-if-n-and-its-double-exist/submissions/
# Check If N and Its Double Exist

arr = [-20,8,-6,-14,0,-19,14,4]
cnt=0

# Condition for counting zeroes separately
for i in arr:
    if i==0:
        cnt+=1
        arr.remove(0)
                
# If count of zero is even.
# Then pass the condition
if cnt>0 and cnt%2==0:
    print("True")
        
for i in arr:
    j = 2*i
            
    if (j in arr):
        print("True")
       
print("False")            