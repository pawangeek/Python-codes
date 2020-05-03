# @Date:   2020-05-03T14:12:07+05:30
# @Last modified time: 2020-05-03T14:20:33+05:30

# https://leetcode.com/contest/biweekly-contest-25/problems/kids-with-the-greatest-number-of-candies/
# Kids With the Greatest Number of Candies

c = [2,3,5,1,3]
ec = 3

mx, res = max(c), []
for i in c:
    res.append(True) if i+ec >= mx else res.append(False)

print(res)
