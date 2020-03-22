# Return the maximum number of four-person families you can allocate on the cinema seats.
# https://leetcode.com/contest/biweekly-contest-22/problems/cinema-seat-allocation/

# Difficulty : Medium
# Concept : Hashmap (Dictionary) + How to remove flag by local list

from collections import defaultdict

n = 3
rev = [[3,7],[2,7],[3,4],[1,1],[1,3],[2,5],[3,1],[2,4],[2,1],[1,8],[2,3]]
d,p = defaultdict(list),[]

# possible seats for family
f1, f2, f3, res = [2,3,4,5], [4,5,6,7], [6,7,8,9], 0

    # fill the dictionary, row as a key and reserved seats as a list
for i in range(len(rev)):
    d[rev[i][0]].append(rev[i][1])

for v in d.values():

    f = [1,1,1]
    for s in v:
        
        if s in f1 and s not in f2: # condition 1
            f[0]=0
        if (s in f2 and s in f1):# condition 2
            f[1],f[0]=0,0
        if (s in f2 and s in f3):
            f[1],f[2]=0,0
        if s in f3 and s not in f2:  # condition 3
            f[2]=0

    # If any of the 1st or 3rd posiiblity 'only' filled than 2nd possibilty never be filled    
    if (f[0]==0 and f.count(0)==1) or (f[2]==0 and f.count(0)==1): 
        f[1]=0

    # if any of seat is not filled then maximum posiible is 2
    if f.count(1)==3:
        y=2 
    else:
        y=f.count(1)

    # storing count of 1 in another list    
    p.append(y) 

print(sum(p)+ 2*(n-len(d))) 

# 2*(n-len(d)) This part is for remaining rows having no booked seats so 
# i.e. Maxm seats possible(2) * no. of remaining rows