# @Date:   2020-05-03T14:21:09+05:30
# @Last modified time: 2020-05-03T14:22:24+05:30

# https://leetcode.com/contest/biweekly-contest-25/problems/max-difference-you-can-get-from-changing-an-integer/
# Max Difference You Can Get From Changing an Integer

import sys
num = 123456

mn, mx = sys.maxsize, -sys.maxsize-1

for i in range(10):
    for j in range(10):

        t = int(str(num).replace(str(i), str(j)))

        if t != 0 and len(str(t)) == len(str(num)):
            mn, mx = min(mn, t), max(mx, t)

print (mx- mn)
