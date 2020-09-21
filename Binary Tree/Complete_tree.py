class Node:

    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

def countnodes(root):

    if root is None:
        return 0

    return (1+countnodes(root.left)+countnodes(root.right))

def iscomplete(root, index, nodes):

    if root is None:
        return True
    
    if index>=nodes:
        return False
    
    return (iscomplete(root.left, 2*index+1, nodes)) and (iscomplete(root.right, 2*index+2, nodes))

root = Node(3)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(8)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(0)

count = countnodes(root)
print(iscomplete(root, 0, count))
    