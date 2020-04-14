# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3293/

# Any path can be written as two arrows (in different directions) from some node, 
# where an arrow is a path that starts at some node and only travels down to child nodes.

# If we knew the maximum length arrows L, R for each child, then the best path touches L + R + 1 nodes.

# Time complexity : O(n)
# Space complexity : O(n)

# Let's calculate the depth of a node in the usual way: max(depth of node.left, depth of node.right) + 1.
# While we do, a path "through" this node uses 1 + (depth of node.left) + (depth of node.right) nodes.
# Let's search each node and remember the highest number of nodes used in some path. 
# The desired length is 1 minus this number.

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1