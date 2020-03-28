# Adamant Vowels of a string are vowels that remain at same index even if string is reversed.
# Concept is to check every reversed letter

t = input()
a1 = [i for i in t]

p = t[::-1]
a2 = [i for i in p]

j, cnt=0, 0
vow = ['a','e','i','o','u']

for i in range(len(a1)):
    if (a1[i] == a2[j]) and (a1[i] in vow) and (a2[j] in vow):
        cnt+=1
        j+=1
    else:
        j+=1
    
print(cnt)