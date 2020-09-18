class Node:

    def __init__ (self, data):
        self.data = data
        self.next = None

class BinaryTree:

    def __init__ (self, data):
        self.left = None
        self.right = None
        self.data = data

class Conversion:

    def __init__ (self, data= None):
        self.head = None
        self.root = None

    def push (self, data):

        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def convertbinary(self):

        q = []

        if self.head is None:
            self.root = None
            return
        
        self.root = BinaryTree(self.head.data)
        q.append(self.root)
