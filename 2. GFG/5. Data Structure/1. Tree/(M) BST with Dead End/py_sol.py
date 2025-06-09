class Solution:
    def isDeadEnd(self, root):
        # Code here
        # Helper function with min and max range
        def dfs(node, min_val, max_val):
            if not node:
                return False
            if min_val == max_val:
                return True
            # Recurse on left and right with updated bounds
            return (dfs(node.left, min_val, node.data - 1) or
                    dfs(node.right, node.data + 1, max_val))

        return dfs(root, 1, float('inf'))