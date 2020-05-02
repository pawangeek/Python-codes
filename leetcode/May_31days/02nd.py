# @Date:   2020-05-02T17:06:47+05:30
# @Last modified time: 2020-05-02T17:08:46+05:30

# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/


J = "aA"
S = "aAAbbbb"

j = list(set(J))
# Simple solution

cnt = 0
for i in S:
    if i in J:
        cnt+=1

print (cnt)
