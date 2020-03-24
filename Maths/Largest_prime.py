# https://practice.geeksforgeeks.org/problems/largest-prime-factor/0

from math import sqrt
for _ in range(int(input())):
    
    n = int(input())
    m = -1

    # Condition for 2 as prime. Continue till it divides by 2
    # Complexity = log(n) (worst)
    while n % 2 == 0: 
        m, n = 2, n//2

    # condition for 3 and more for prime
    for i in range(3, int(sqrt(n)) + 1, 2):

        # contine till if particular number divide 
        while n%i == 0: 
            m, n = i, n/i 
      
    if n > 2: 
        m = n 
      
    print (int(m)) 