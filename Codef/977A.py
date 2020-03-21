#https://codeforces.com/problemset/problem/977/A

m,n = map(int,input().split())
 
for i in range(n):
    if m%10==0:
        m=m/10
    else:
        m=m-1
        
print(int(m))