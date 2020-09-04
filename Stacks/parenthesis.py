for _ in range(int(input())):
    
    s = list(input())
    
    flag = 0
    stack = []
    mappings = {"]":"[", "}":"{", ")":"("}
    
    for char in s:
        
        if char in mappings:
            
            top = stack.pop() if stack else '#'
            
            if mappings[char] != top:
                flag = 1
                break
                
        else:
            stack.append(char)
    
    if stack or flag==1:
        print("not balanced")
    else:
        print("balanced")