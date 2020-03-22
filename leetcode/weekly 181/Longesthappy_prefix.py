# A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

# Difficulty (i) Easy-Brute force (Space:O(n))
#            (ii) Medium - Rolling Hash (Space:O(1))
#            (iii)Hard - Z Algo, KMP Optim

# https://leetcode.com/contest/weekly-contest-181/problems/longest-happy-prefix/



# (i) Brute force

s = input()
re = ''

for i in range(1,len(s)):
    if s[:i]==s[-i:]:
        r=s[:i]
print(re)

# Just check if prefix is same as suffux in a loop and every time it replace it by maximum of that


# (ii) Rollong Hash (Sliding window concept)
# Explanantion : https://www.quora.com/What-is-a-rolling-hash-and-when-is-it-useful

l,r,mod,res=0,0,(10**9)+7,0

for i in range(len(s)-1):
    l=(l*128+ord(s[i])) % mod
    r = (r + pow(128, i, mod) * ord(s[~i])) % mod
    if l == r: 
        res = i + 1

print(s[:res])

