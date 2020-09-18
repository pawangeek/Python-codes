from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def invert(root):

    # Create a empty queue for level order traversal
    queue = deque()
    queue.append(root)

    while queue:

        node = queue.popleft()

        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

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

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(4)  
    root.left.right = Node(5)   

    levelorder(root)
    root = invert(root)
    levelorder(root)