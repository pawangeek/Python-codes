dicts = ['POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN']
start = 'TOON'
target = 'PLEA'

def isadjacent(word1, word2):
    
    mismatch = [1 for w1, w2 in zip(word1, word2) if w1 != w2 ]
    return (len(mismatch)==1)

def wordladder(dicts, start, target):
    
    # To check word present in d or not
    if target not in dicts:
        return 0
        
    # If present
    stack, count = [], 0
    stack.append(start)
    
    while stack:
        word = stack.pop()
        
        for i in dicts:
            
            # Check dist between both words
            if isadjacent(word, i):
                count += 1
                
                dicts.remove(i)
                stack.append(i)
                
                if stack[-1]==target:
                    return count+1
                    
    return 0
                    
print(wordladder(dicts, start, target))            
    