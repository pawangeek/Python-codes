def remAnagram(str1,str2):
    
    alph = [0 for i in range(26)]
    
    for i in str1:
        alph[ord(i)-ord('a')]+=1
        
    for i in str2:
        alph[ord(i)-ord('a')]-=1
        
    return sum(map(abs, alph))
    