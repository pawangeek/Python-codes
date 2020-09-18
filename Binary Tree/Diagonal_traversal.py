# The idea is to use a queue to store only the left child of current node. 
# After printing the data of current node make the current node to its right child, if present.
# A delimiter NULL is used to mark the starting of next diagonal.

from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diagonal(root):

    if root is None:
        return
    
    queue = deque()

    queue.append(root)
    queue.append(None)

    while queue:

        node = queue.popleft()

        if not node:
            if not queue:
                return
            
            print(' ')
            queue.append(None)

        else:
            while node:
                print(node.data, end = ' ')

                if node.left:
                    queue.append(node.left)

                node = node.right

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(4)  
    root.left.right = Node(5)   

    diagonal(root)