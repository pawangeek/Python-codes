# @Date:   2020-04-26T23:34:45+05:30
# @Last modified time: 2020-04-26T23:35:44+05:30

s = '011101'
a = 0
for i in range(1,len(s)):

    b = s[:i].count('0')
    c = s[i:len(s)].count('1')
    a = max(a,b+c)

print(a)
