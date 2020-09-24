for _ in range(int(input())):
    
    s = input()
    l = len(s)
    
    dp = [[0 for i in range(l)] for i in range(l)]
    maxlen = 1
    
    # Initially all of words are one letter palindrome
    # So maxlength is equal to 1
    for i in range(l):
        dp[i][i] = 1
        start = i
        
    # Now for checking two length we check prev with curr letter
    # If same than maxlen become 2 and their first occurance become start
    for i in range(l-1):
        if s[i]==s[i+1]:
            dp[i][i+1] = 1
            
            if maxlen<2:
                start = i
                maxlen = 2

    # Now for rest of lengths we check them in loop 
    for k in range(3, l+1):
        i = 0
        
        # Take i and run till (n-k) 
        # Since for 8 char string check from i varies from 0 to 6
        while i<l-k+1:
            
            # Now and j varies with 2, 8 as in our above example
            # for boundaries
            j = i+k-1
            
            # Now if both the char are same (i, j) than we check for the substring b/w them
            # And that substring is palindrome if we have 1 on dp table for that
            if s[i]==s[j] and dp[i+1][j-1]==1:
                dp[i][j]=1
                
                # If occur store max(k) an it's starting point
                if k>maxlen:
                    maxlen = max(maxlen, k)
                    start = i
                    
            i+=1
                    
    print(s[start:start+maxlen]) if maxlen>1 else print(s[0])
