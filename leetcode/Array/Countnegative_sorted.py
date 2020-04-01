# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
# Return the number of negative numbers in grid.

# worst case : O(m*n)
grid=[]

cnt=0
for i in grid:
    for j in range(len(i)):
        if i[j]<0:
            cnt+=len(i)-(j)
            break
        
print (cnt)

# Alternate solution using bisect
# Complexity : O(m*logn)
        