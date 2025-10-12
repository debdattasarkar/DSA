'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def distCandy(self, root):
        """
        Postorder DFS.
        For each node:
          - get left_net, right_net
          - moves += |left_net| + |right_net|
          - return node.data - 1 + left_net + right_net

        Time  : O(n)  (visit each node once)
        Space : O(h)  recursion stack (h = tree height; worst O(n) if skewed)
        """
        self.moves = 0  # global accumulator of edge flows

        def dfs(node):
            if not node:
                return 0  # null contributes no flow

            # Postorder: process children first
            left_net  = dfs(node.left)   # O(size of left)
            right_net = dfs(node.right)  # O(size of right)

            # All flow across edges to children counts as moves
            self.moves += abs(left_net) + abs(right_net)

            # Return this subtree's net balance up to its parent
            return node.data - 1 + left_net + right_net

        dfs(root)    # O(n)
        return self.moves