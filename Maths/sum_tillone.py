# Task : Repeatedly add all its digits until the result has only one digit.

for i in range(int(input())):
    p = (int(input()))%9
    print(9) if p==0 else print(p)