from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertion(root, key):

    if root is None:
        return Node(key)

    else:

        if root.data == key:
            return root

        elif root.data > key:
            root.left = insertion(root.left, key)

        else:
            root.right = insertion(root.right, key)

    return root

def levelorder(root):

    queue = deque()
    queue.append(root)

    while queue:

        print(queue[0].data, end = ' ')
        node = queue.popleft()

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    print()


def deletion(root, key):

    if root is None:
        return root

    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
    if key < root.data:
        root.left = deletion(root.left, key)

    # If the kye to be delete is greater than the root's key 
    # then it lies in right subtree 
    elif key > root.data:
        root.right = deletion(root.right, key)

    # If key is same as root's key, then this is the node 
    # to be deleted 
    else:

        # Two cases for zero or one child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Get inorder successor of node with two children
        temp = root.right

        while temp.left:
            temp = temp.left

        root.data = temp.data
        root.right = deletion(root.right, temp.data)

    return root


root = Node(50)
root = insertion(root, 30)
root = insertion(root, 20)
root = insertion(root, 40)
root = insertion(root, 70)
root = insertion(root, 60)
root = insertion(root, 80)

levelorder(root)

root = deletion(root, 70)

levelorder(root)

