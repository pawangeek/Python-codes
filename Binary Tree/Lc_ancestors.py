class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def recurse(node):

    if node is None:
        return False

    left = recurse(node.left)
    right = recurse(node.right)

    mid = node==n1 or node==n2

    if mid+left+right>=2:
        ans = node

    return mid or left or right

def lca(root, n1, n2):

    ans = -1
    recurse(root, n1, n2, ans)
    return ans

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(4)  
    root.left.right = Node(5)   

    print(lca(root, 4, 3))