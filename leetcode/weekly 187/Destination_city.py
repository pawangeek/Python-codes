# @Date:   2020-05-03T21:18:23+05:30
# @Last modified time: 2020-05-03T21:28:11+05:30

# https://leetcode.com/contest/weekly-contest-187/problems/destination-city/
# Destination-city

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

from collections import Counter

lst, bck = [], []
     
for i in paths:
    bck.append(i[1])
    lst.extend([i[0],i[1]])

arr = Counter(lst)

for k,v in arr.items():
    if v==1 and k in bck:
        print(k)
        break
