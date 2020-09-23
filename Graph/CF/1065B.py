# maxm and minm isolated components given no of vertices and edges

"""
APPROACH

(i) For minm if more than half of vertices than 0 else reduce 2*e from vertices
(ii) Since we know maxm edges in undirected graph can be formed are n*(n-1)/2 (without self loop and multigraph)
(iii) So By reversing that condition solve the quadratic equation to find minm 
        vertices can be join to get our maxm isolated components
"""
import math

v, e = map(int, input().split())

root = (1+math.sqrt(1+(8*e)))/2
maxm = math.ceil(root)
maxm = maxm if e>0 else maxm-1

minm = v-(2*e) if e<math.ceil(v/2) else 0

print(minm, v-maxm)