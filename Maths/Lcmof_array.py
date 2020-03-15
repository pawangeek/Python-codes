# Task : To find the lcm of array
# Formula lcm = a*b/gcd(a,b)

from math import gcd

t = int(input())
arr = list(map(int,input().split()))

lcm = arr[0]

for i in arr[1:]:
    lcm = int(lcm*i)//gcd(lcm,i)

print(lcm)