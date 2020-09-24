# Can be formulated as Fibonacci no.
n = int(input())

# (O(1)) Approach
binet = (1 + 5 ** 0.5) / 2
print(int((binet ** n + 1) / 5 ** 0.5))


# Iterative

if n==1:
    print(1)

elif n==2:
    print(2)

else:
    a = 1
    b = 2

    for i in range(n-2):
        b,a = b+a,b

    print(b)