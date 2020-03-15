# Problem is to find prime numbers that are in arrays pf numbers

t = int(input())
arr = list(map(int,input().split()))

for j in arr:

    d,primes=[],[]
    for i in range(2,j+1):

        if i not in d:
            primes.append(i)

            for i in range(i*i,j-1,2):
                d.append(i)

print(list(set(primes)))