# https://leetcode.com/problems/reformat-the-string/
s = "covid2019"

a, b = [], []
for c in s:
    if 'a' <= c <= 'z':
        a.append(c)
    else:
        b.append(c)

if len(a) < len(b):
    a, b = b, a
if len(a) - len(b) >= 2:
    print ('')

ans = ''
for i in range(len(a)+len(b)):
    if i % 2 == 0:
        ans += a[i//2]
    else:
        ans += b[i//2]
print(ans)