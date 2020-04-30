# @Date:   2020-04-30T16:45:57+05:30
# @Last modified time: 2020-04-30T16:53:52+05:30

# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Binary Tree Maximum Path Sum

# Beautiful Explaination
# https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram

def maxPathSum(self, root):
    if not root:
        return 0
    self.res = root.val
    self.oneSum(root)
    return self.res

# compute one side maximal sum,
# (root+left children, or root+right children),
# root is the included top-most node

def oneSum(self, node):
    if not node:
        return 0
    l = max(0, self.oneSum(node.left))
    r = max(0, self.oneSum(node.right))
    self.res = max(self.res, node.val+l+r)
    return node.val + max(l, r)
