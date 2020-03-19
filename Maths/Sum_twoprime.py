# Task : Return no. as sum of two prime numbers
# Approach : (i)To find all position of prime numbers in whole range using sieve of eratos
#            (ii) Rup loop to half of numbers and get those numbers whole sum is 2 in prev stored array

arr = [1]*10001
for i in range(2,len(arr)):
    
    if arr[i]==1:
        for j in range(i*i,len(arr),i):
            arr[j]=0

for _ in range(int(input())):
    p = int(input())

    for i in range(3,p//2):
        if arr[i]+arr[p-i]==2:
            print(i,p-i)
            break