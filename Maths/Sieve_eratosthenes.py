# Working : first we iterate through all numbers to n, and one by one exclude non-prime numbers by storing them in a list

t = int(input())
d=[]

for i in range(2,t+1):

    if i not in d:
        print(i)

        for j in range(i*i,t+1,i):
            d.append(j)