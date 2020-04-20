# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Construct Binary Search Tree from Preorder Traversal

# Give the function a bound the maximum number it will handle.
# The left recursion will take the elements smaller thn node.val
# The right recursion will take the remaining elements smaller than bound

class Solution:
    i = 0
    def bstFromPreorder(self, A, bound=float('inf')):
        if self.i == len(A) or A[self.i] > bound:
            return None
        root = TreeNode(A[self.i])
        self.i += 1
        root.left = self.bstFromPreorder(A, root.val)
        root.right = self.bstFromPreorder(A, bound)
        return root
        