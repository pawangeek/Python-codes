# https://www.interviewbit.com/problems/balance-array/
peven = podd =seven = sodd = res = 0
A = [5, 5, 2, 5, 8]

for n,i in enumerate(A):
    if n%2==0:
        peven += i
    else:
        podd += i
        
        
for n,i in enumerate(A):
    
    if n%2==0:
        peven -= i
    else:
        podd -= i
        
    if peven+sodd==podd+seven:
        res+=1
        
    if n%2==0:
        seven += i
    else:
        sodd += i
        
print (res)