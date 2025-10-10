'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root): 
        """
        Returns the maximum path sum in the tree.
        Approach: single DFS computing:
          - best_down_gain(node): best sum of a path that starts at 'node' and goes down one side
          - updates a nonlocal/global 'max_overall' with the best path that passes through 'node'
        Time  : O(n)  -- visit each node exactly once
        Space : O(h)  -- recursion stack, h = tree height (O(n) worst-case, O(log n) average if balanced)
        """
        self.max_overall = float('-inf')  # tracks best path seen anywhere

        def dfs(node):
            if not node:
                return 0  # a null contributes 0 downward gain

            # Recursively compute the best downward gains from children
            left_gain  = dfs(node.left)   # O(size(left))
            right_gain = dfs(node.right)  # O(size(right))

            # If a downward gain is negative, we drop it (use 0)
            left_gain  = max(0, left_gain)
            right_gain = max(0, right_gain)

            # Path that "passes through" this node (can take both sides)
            path_through_node = node.data + left_gain + right_gain

            # Update global maximum path sum
            if path_through_node > self.max_overall:
                self.max_overall = path_through_node

            # Return the best single-branch gain to parent (choose one side)
            best_down_gain = node.data + max(left_gain, right_gain)
            return best_down_gain

        dfs(root)
        return self.max_overall