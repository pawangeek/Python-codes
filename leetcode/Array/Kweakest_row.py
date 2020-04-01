# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# The K Weakest Rows in a Matrix

# Important : (i) How to sort a dictionary acoording to values and get keys as list (Print statement)
#             (ii) Updating values in dict in python .update({key:value})

mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 2

p={}

# Updating relevant position and number of 1(sum) as keys and values respectivelt
for n,i in enumerate(mat):
    p.update({n:sum(i)})

# sort according to values and get keys
print ((sorted(p, key=p.get))[:k])