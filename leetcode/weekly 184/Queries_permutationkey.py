# Queries on a Permutation With Key
# https://leetcode.com/contest/weekly-contest-184/problems/queries-on-a-permutation-with-key/

queries = [7,5,5,8,3]
m = 8

now,res = list(range(1, m + 1)),[]

for i in queries:
    x = now.index(i)
    res.append(x)
    now = [i] + now[:x] + now[x + 1 :]

print(res)