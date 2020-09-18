class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def depth(node, ans):
    if not node:
        return 0

    left = depth(node.left, ans)
    right = depth(node.right, ans)

    ans = max(ans, left+right+1)
    return max(left, right)+1

def diameter(root):

    ans = 1

    depth(root, ans)
    return ans-1

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(4)  
    root.left.right = Node(5)   

    print(diameter(root))