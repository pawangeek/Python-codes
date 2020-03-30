# Useful for first occurance in string
# Don't tell overlapping patterns 

h = input()
n= input()

# Example : ababaaaabbabaaabababaab
# Pattern : baab

# Iterate loop till remaining chars are equal to lenght to pattern
for i in range(0, len(h) - len(n) + 1):
    if h[i:i+len(n)] == n:
        print (i)