# <left subtree> <root> <right subtree>

# Create an empty stack s
# Initialize current node as root

# Push current node to S and set curr=curr->left

# If curr is NULL and stack is not empty
# (i) Pop the top and print
# (ii) Set curr = popped->right

# If curr is NULL and stack is empty


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):

    curr = root
    stack = []

    while True:

        # reach the left most node of curr
        if curr is not None:
            stack.append(curr)
            curr = curr.left

        elif stack:

            curr = stack.pop()
            print(curr.data, end = ' -> ')

            curr = curr.right

        else:
            break

    print(None)

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5) 

    inorder(root)