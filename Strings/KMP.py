# http://www.btechsmartclass.com/data_structures/knuth-morris-pratt-algorithm.html

# Use to detect pattern of string
# Running Time is O(n+m), where 'n' is length of the searched text (typically large) and 'm' is the length of pattern
 
# Space: O (n) - to store tracker array, n is the length of substring
# Naive do it in O(n^2)

word = input() # For string
pattern = input() # For pattern you want to search

# Getting lenghs of both string and pattern
m,n = len(word),len(pattern)

# create lps[] (size of pattern) that will hold the longest prefix suffix  values for pattern 
lps_array = [0]*n
j,i = 0,1

# for index 0, it will always be 0 so starting from index 1
# By setting value of i=1
while i<n:

    if pattern[i]==pattern[j]:
        lps_array[i]=j+1
        j,i=j+1,i+1
    else:
        if j>0:
            j = lps_array[j-1]
        else:
            lps_array[i]=0
            i +=1

i, j = 0, 0
while i < m:

    # current characters match, move to the next characters
    if word[i]==pattern[j]:
        i, j = i+1, j+1

    if j == n:
        print (i - j)
        j = lps_array[j-1]

    # current characters don't match
    elif i < m and pattern[j] != word[i]:

        # try start with previous longest prefix
        if j > 0:  
            j = lps_array[j - 1]
        
        # 1st character of pattern doesn't match character in text, go to the next character in text
        else:
            i += 1