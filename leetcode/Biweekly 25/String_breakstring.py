# @Date:   2020-05-03T15:00:04+05:30
# @Last modified time: 2020-05-03T15:38:29+05:30

# https://leetcode.com/contest/biweekly-contest-25/problems/check-if-a-string-can-break-another-string/
# Check If a String Can Break Another String

s1 = "abc"
s2 = "xya"

a1 = sorted([c for c in s1])
a2 = sorted([c for c in s2])
check = 0

for i in range(len(a1)):

    if a1[i] == a2[i]:
        continue

    if c1 == 0:
        c1 = 1 if a1[i] > a2[i] else -1

    else:
        c2 = 1 if a1[i] > a2[i] else -1
        if c1 * c22 == -1:
            print (False)

print(True)
