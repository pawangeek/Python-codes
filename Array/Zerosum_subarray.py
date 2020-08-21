# Given an array of integers, check if array contains a sub-array having 0 sum.

A = [4, -6, 3, -1, 4, 2, 7]

s = set(0)
sum = 0

for i in A:

    sum+=i

    if sum in s:
        print("True")
        break

    s.add(sum)

print("False")