'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def transformTree(self, root):
        """
        Reverse inorder (Right -> Node -> Left) with a running suffix sum.
        For each node: new_value = sum of strictly greater keys.
        Time  : O(n)   -- each node visited once
        Space : O(h)   -- recursion stack, h = tree height
        """
        greater_sum = 0  # sum of all nodes visited so far (greater than current)

        def rev_inorder(node):
            nonlocal greater_sum
            if not node:
                return
            # Visit larger keys first
            rev_inorder(node.right)

            # Update this node to sum of greater keys
            original = node.data
            node.data = greater_sum
            greater_sum += original

            # Then smaller keys
            rev_inorder(node.left)

        rev_inorder(root)
        return root
