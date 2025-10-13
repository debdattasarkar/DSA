'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getMaxSum(self, root):
        """
        For each node, return (take, skip):
          take = node.data + skip_left + skip_right
          skip = max(take_left, skip_left) + max(take_right, skip_right)

        Time  : O(n)   each node processed once
        Space : O(h)   recursion stack (h = tree height)
        """
        def dfs(node):
            if not node:
                # (take, skip) for empty subtree
                return (0, 0)

            take_l, skip_l = dfs(node.left)   # postorder
            take_r, skip_r = dfs(node.right)

            take_here = node.data + skip_l + skip_r
            skip_here = max(take_l, skip_l) + max(take_r, skip_r)
            return (take_here, skip_here)

        take_root, skip_root = dfs(root)
        return max(take_root, skip_root)