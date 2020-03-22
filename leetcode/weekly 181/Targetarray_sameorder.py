# Given two arrays of integers nums and index. Your task is to create target array 
# Difficulty: very easy
# Concept : I/o

# https://leetcode.com/contest/weekly-contest-181/problems/create-target-array-in-the-given-order/

nums = list(map(int,input().split()))
index = list(map(int,input().split()))

p =[]
for i in range(len(nums)):
    p.insert(index[i],nums[i])
            
print(p) 