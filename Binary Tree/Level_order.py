from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelorder(root):

    # Create a empty queue for level order traversal
    queue = deque()
    queue.append(root)

    while queue:

        # Get the first data from queue
        print(queue[0].data, end = ' ')
        node = queue.popleft()

        # if node-> left is present than append
        if node.left:
            queue.append(node.left)

        # if node-> right is present than append
        if node.right:
            queue.append(node.right)

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(4)  
    root.left.right = Node(5)   

    levelorder(root)