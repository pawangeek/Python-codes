from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def spiralorder(root):

    if not root:
        return

    queue = deque()
    queue.append(root)
    flag = True

    while queue:

        count = len(queue)
        ans = []

        for _ in range(count):

            node = queue.popleft()
            ans.append(node.data)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        print(*(ans)) if flag else print(*(ans[::-1]))
        flag = False if flag else True

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    spiralorder(root)