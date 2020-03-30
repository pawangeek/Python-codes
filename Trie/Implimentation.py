# It is a tree-like structure where each node represents a single character of a given string. 
# And unlike binary trees, a node may have more than two children.

class Trienode(object):
    
    def __init__(self, char):
        self.char = char
        self.children=[]

        # Is it the last character of the word.
        self.word_finish = False

        # How many times this character appeared in the addition process
        self.counter = 1

def add(root,word):
        
    node = root
    for char in word:

        found_in_child = False

        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:

                # We found it, increase the counter by 1
                child.counter+=1

                # And point the node to the child that contains this char
                node = child
                found_in_child = True
                break

        if not found_in_child:
            new_node = Trienode(char)
            node.children.append(new_node)

            # And then point node to the new child
            node = new_node
            
    # Every thing finished mark it as word finish
    node.word_finish = True

def find_prefix(root,prefix):

    node=root

    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False,0

    for char in prefix:
        char_not_found=True

        # Search through all the children of the present `node`
        for child in node.children:
            if child.char==char:

                # We found the char existing in node
                char_not_found = False

                # Assign node as the child containing the char and break
                node = child
                break
                
        if char_not_found:
            return False,0
        
    return True,node.counter

if __name__ == "__main__":
    root = Trienode('*')
    add(root, "ahishers")
    #add(root, 'hack')

    print(find_prefix(root, 'his'))
    print(find_prefix(root, 'he'))
    print(find_prefix(root, 'she'))
    print(find_prefix(root, 'hers'))
    #print(find_prefix(root, 'happy'))