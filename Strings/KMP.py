# Use to detect pattern of string
# Running Time is O(n+m), where 'n' is length of the searched text (typically large) and 'm' is the length of pattern
 
# Space: O (n) - to store tracker array, n is the length of substring
# Naive do it in O(n^2)

word = input() # For string
pattern = input() # For pattern you want to search

# Getting lenghs of both string and pattern
m,n = len(word),len(pattern)
print(m)

# create lps[] that will hold the longest prefix suffix  values for pattern 
prefix_table = [0]*m
prefix_count = 0

for i in range(1,m):
    print(word[i],word[prefix_count])

    if word[i]==word[prefix_count]:
        prefix_count+=1
    else:
        prefix_count=0

    prefix_table[i] = prefix_count

print(prefix_table)

j, positions = 0,[]
for i in range(m):
    if pattern[j]==word[i]:
        if j == len(pattern)-1:
            positions.append(i+1-len(pattern))
        
        else:
            j+=1
    else:
        j = prefix_table[j-i]
    
print(positions)