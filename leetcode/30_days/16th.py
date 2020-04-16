# Valid Parenthesis String
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3301/

s = "(*))"    

# stack 1, try to test all the ( and * can balance all the )
S,f=[],0        

# go through s from left to right
for x in s:
    if x=='(' or x=='*':
        S.append(x)
    else:
        if len(S)>0:
            S.pop()
        else:
            f = 1        # this means left ( is not enough
    
# stack 2, try to test all the ) and * can balance all the (
S=[]        
    
# go through s from right to left
for x in s[::-1]:
    if x==')' or x=='*':
        S.append(x)
    else:
        if len(S)>0:
            S.pop()
        else:
            f = 1       # this means right ) is not enough
    
print(f==0)