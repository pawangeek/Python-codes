# It is a tree-like structure where each node represents a single character of a given string. 
# And unlike binary trees, a node may have more than two children.

class Trienode(object):
    
    def __init__(self, char):
        self.char = char
        self.children=[]

        # Is it the last character of the word.
        self.word_finish = False

        # How many times this character appeared in the addition process
        self.counter = 0