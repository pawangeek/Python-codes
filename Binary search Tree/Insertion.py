class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def insertion(root, key):

    if root is None:
        return Node(key)

    else:
        if root.data == key:
            return root

        elif root.data < key:
            root.right = insertion(root.right, key)

        else:
            root.left = insertion(root.left, key)

    return root

def inorder(root):

    if root:
        inorder(root.left)
        print(root.data, end = ' ')

        inorder(root.right)

r = Node(50)
r = insertion(r, 30)
r = insertion(r, 20)
r = insertion(r, 40)
r = insertion(r, 70)
r = insertion(r, 60)
r = insertion(r, 80)

(inorder(r))