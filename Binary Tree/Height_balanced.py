class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check(root):

    if root is None:
        return 0

    left = check(root.left)
    right = check(root.right)

    if left == -1 or right == -1 or abs(left-right) > 1:
        return -1

    return 1+ max(left, right)

def balanced(root):
    return (check(root)!=-1)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(4)

    print(balanced(root))