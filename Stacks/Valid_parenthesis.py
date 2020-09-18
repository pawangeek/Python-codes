for _ in range(int(input())):
    
    s = list(input())
    
    flag = 0

    # to keep track of opening brackets
    stack = []

    # Hashmap for keeping track of mappings
    mappings = {"]":"[", "}":"{", ")":"("}
    
    for char in s:
        
        # if character is closing bracket
        if char in mappings:
            
            # pop topmost element from stack
            # Else dummy variable
            top = stack.pop() if stack else '#'
            
            # if mapping don't match from top of stack
            if mappings[char] != top:
                flag = 1
                break

        # if character is not closing bracket        
        else:
            stack.append(char)
    
    # if stack is not empty
    if stack or flag==1:
        print("not balanced")
    else:
        print("balanced")