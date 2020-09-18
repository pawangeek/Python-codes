from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def symmetric(root):

    # Create a empty queue for level order traversal
    queue = deque()
    queue.append(root)
    queue.append(root)

    while queue:

        # Get the first data from queue
        node1 = queue.popleft()
        node2 = queue.popleft()

        # if both nodes are not present
        if not node1 and not node2:
            continue

        # If any of nodes at same level is not present
        if not node1 or not node2:
            return False

        # If there data is not same
        if node1.data != node2.data:
            return False

        queue.append(node1.left)
        queue.append(node2.right)
        queue.append(node1.right)
        queue.append(node2.left)

    return True

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)  
    root.right = Node(2)  
    root.left.left = Node(4)  
    root.left.right = Node(5)  
    root.right.left = Node(5)  
    root.right.right = Node(4) 
    
    print(symmetric(root))