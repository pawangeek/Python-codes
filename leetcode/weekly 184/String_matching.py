# https://leetcode.com/contest/weekly-contest-184/problems/string-matching-in-an-array/
# Given an array of string words. Return all strings in words which is substring of another word in any order. 

words = ["mass","as","hero","superhero"]

res = []
for s in words:
    for w in words:
        if s != w and s in w:
            res.append(s)
            break

if len(res) != 0:
    print(res)
else:
    print([])