from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def verticaltrav(root):

    # Create a empty queue for level order traversal
    queue = deque()
    queue.append((root, 0))
    dic = {}

    while queue:

        node, dist = queue.popleft()

        if node.left:
            queue.append((node.left, dist-1))

        if node.right:
            queue.append((node.right, dist+1))

        if dist in dic:
            dic[dist].append(node.data)
        else:
            dic[dist] = [node.data]

    for k in sorted(dic.keys()):
        print(k, dic[k])         

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(4)  
    root.left.right = Node(5)   

    verticaltrav(root)