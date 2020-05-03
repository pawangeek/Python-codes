# @Date:   2020-05-03T14:00:00+05:30
# @Last modified time: 2020-05-03T14:08:41+05:30

# https://leetcode.com/problems/ransom-note/
# Ransom NOTE

# nlogn approach
# we can do it easily in o(n) by popping from m or making counter

r="fffbfg"
m="effjfggbffjdgbjjhhdegh"

# Edge case when r is empty
if not r:
    return True

r = ''.join(sorted(r))
m= ''.join(sorted(m))

j,cnt = 0,0
for i in m:

    if i==r[j]:
        cnt+=1
        j+=1

    if cnt==len(r):
        return True

return False
