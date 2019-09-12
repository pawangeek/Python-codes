from collections import deque
t = int(input())

while t:
    l = input()
    myb = deque()
    
    count = 1
    
    for i in l:
        if i=='(':
            print(count,end=' ')
            myb.append(count)
            count+=1
            
        elif i==')':
            print(myb.pop(), end =' ')
     
    print()       
    t-=1
    
    
    