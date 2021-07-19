"""
Input:
str1 = "fodr", str2="gork"
k = 2

Output:
True

Explanation: Can change fd to gk
"""

def areKAnagrams(str1, str2, k):
    
    alph1 = [0 for i in range(26)]
    alph2 = [0 for i in range(26)]
    
    # If length cant same we never
    if (len(str2)!= len(str1)) :
        return False
        
    for i in str1:
        alph1[ord(i)-ord('a')]+=1
        
    for i in str2:
        alph2[ord(i)-ord('a')]+=1
    
    count = 0
    for i in range(len(alph1)):
        if alph1[i]>alph2[i]:
            count += abs(alph1[i]-alph2[i])

    return (count<=k)
