class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check(root1, root2):

    if not root1 and not root2:
        return True

    elif not root1 and root2 or not root2 and root1:
        return False

    if root1.data != root2.data:
        return False

    left = check(root1.left, root2.left)
    right = check(root1.right, root2.right)

    return left and right

def subtree(tree, sub):

    if not tree:
        return False
    
    if tree.data == sub.data and check(tree, sub):
        return True

    return subtree(tree.left, sub) or subtree(tree.right, sub)

def subtreecheck(tree, sub):
    return subtree(tree,sub)

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(4)  
    root.left.right = Node(5) 

    root1 = Node(2)
    root1.left = Node(4)  
    root1.right = Node(5)  

    print (subtreecheck(root, root1))