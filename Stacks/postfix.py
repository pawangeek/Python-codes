from collections import deque
import operator

ops = { '+': operator.add, '-': operator.sub, 
        '*': operator.mul, '/': operator.floordiv }
        
t = int(input())

while t:
    l = input()
    mys = deque()
    
    def postfix(l):
        for i in l:
            if i.isdigit():
                mys.append(i)
                
            else:
                v1 = mys.pop()
                v2 = mys.pop()
                
                mys.append(str(ops[i](int(v2),int(v1))))
            
        return int(mys.pop())
    
    print(postfix(l))
    t-=1
            