# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.
# If there is no such integer in the array, return 0.

# Difficulty : easy, 
# Concept : Number Theory

# https://leetcode.com/contest/weekly-contest-181/problems/four-divisors/

import math
arr = list(map(int,input().split()))
        
c=[]
for i in arr: # Iterating through given list

    p=[]
    for j in range(1,math.floor(math.sqrt(i))+1): # Iterating to all numbers in square root(n)
        if i%j==0:
            p.append(i//j)
            p.append(j)
             
    if len(list(set(p)))==4:
        c.append(sum(list(set(p))))
                
print(sum(c))   

# Idea behund iterating to root(n) is that factors covers half from both sides

# Suppose if number is 28 than
# i) first iteration i=1, 28%1==0 (True), Append(28//1) = 28 and Append(1)
# ii) Second iteration i=2, 28%2==0 (True) Append(28//2) = 14 and Append(2)