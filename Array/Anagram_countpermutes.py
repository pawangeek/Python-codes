# Task : To count occurance of anagrams 
# for example in aaba in aabaabaa occurs 4 times

# My approach : Get no. of letters that are equal to given anagram, compute all permutations and match 
# Getting TLE

from itertools import permutations
t = int(input())

def checkana(x):
    final = list(permutations(x,l))
    return final

while t:
    p = input()
    s = input()
    
    ns = [h for h in s]
    l,d,c = len(s),[],0
    
    for i in p:
        d.append(i)
        if len(d)==l:
            f = list(map(list,checkana(d))) # Changing list of tuples to list of lists
            
            if ns in f:
                c+=1
                
            d.pop(0)
        
    print(c)
    
    t-=1