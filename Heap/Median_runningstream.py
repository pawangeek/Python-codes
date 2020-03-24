from heapq import heappush, heappop, heapify
import math

mh, maxh, m=[],[], 0 
for _ in range(int(input())):
    e=int(input())
    
    if len(maxh)>len(mh):
        if e<m:
            heappush(mh,heappop(maxh))
            heappush(maxh,-1*e)
            
        else:
            heappush(mh,e)
            
        m=math.floor((-1*maxh[0]+mh[0])/2)
        
    elif len(mh)==len(maxh):
        if e<m:
            heappush(maxh,-1*e)
            m=-1*maxh[0]
        
        else:
            heappush(mh,e)
            m=mh[0]
        
    else:
        if e>m:
            heappush(maxh,-1*heappop(mh))
            heappush(mh,e)
            
        else:
            heappush(maxh,-1*e)
    
        m=math.floor((-1*maxh[0]+mh[0])/2)

    print(m)