from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def linelevelorder(root):

    queue = deque()
    queue.append(root)

    while queue:

        length = len(queue)

        for _ in range(length):

            node = queue.popleft()
            print(node.data, end=' -> ')

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        print(None)

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(4)  
    root.left.right = Node(5)   

    linelevelorder(root)