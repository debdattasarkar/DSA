'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def removekeys(self, root, l, r):
        """
        Trim BST so all keys lie in [l, r].
        Time  : O(n)  -- each node visited at most once
        Space : O(h)  -- recursion stack, h = tree height (worst O(n))
        """
        if not root:
            return None

        # If this node is too small, discard left subtree; keep trimmed right.
        if root.data < l:
            return self.removekeys(root.right, l, r)

        # If this node is too large, discard right subtree; keep trimmed left.
        if root.data > r:
            return self.removekeys(root.left, l, r)

        # Node is in range: recursively trim children and keep node.
        root.left  = self.removekeys(root.left,  l, r)
        root.right = self.removekeys(root.right, l, r)
        return root