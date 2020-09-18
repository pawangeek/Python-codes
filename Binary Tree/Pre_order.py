from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):

    queue = deque()
    queue.append(root)

    while queue:

        node = queue.pop()
        print(node.data, end = ' ')

        if node.right:
            queue.append(node.right)

        if node.left:
            queue.append(node.left)

    print()

def preorderutil(root):

    if not root:
        return
    
    print(root.data, end= ' ')

    preorderutil(root.left)
    preorderutil(root.right)

def preorderrecur(root):
    preorderutil(root)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    preorder(root)
    preorderrecur(root)