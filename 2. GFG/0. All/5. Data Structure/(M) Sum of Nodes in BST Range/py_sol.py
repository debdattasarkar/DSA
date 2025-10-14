"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def nodeSum(self, root, l, r):
        """
        BST-aware recursion with pruning.
        If node.val < l  -> skip left
        If node.val > r  -> skip right
        Else include node and visit both sides.

        Time  : O(m)  where m is number of visited nodes (≤ n; often much less due to pruning)
        Space : O(h)  recursion stack, h = tree height (worst O(n), avg O(log n) if balanced)
        """
        def dfs(node):
            if not node:
                return 0

            if node.data < l:
                # Entire left subtree < l -> ignore
                return dfs(node.right)
            if node.data > r:
                # Entire right subtree > r -> ignore
                return dfs(node.left)

            # In range: include node and search both sides
            return node.data + dfs(node.left) + dfs(node.right)

        return dfs(root)