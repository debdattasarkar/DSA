"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
from collections import deque

class Solution:
    def levelOrder(self, root):
        # Your code here
        # Edge case: empty tree => return empty list
        if root is None:
            return []

        ans = []
        q = deque([root])  # queue for BFS; O(n) worst-case memory

        while q:
            level_size = len(q)       # number of nodes on current level
            level_vals = []           # collects values for this level

            for _ in range(level_size):
                node = q.popleft()    # O(1)
                level_vals.append(node.data)

                # push children if present
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level_vals)    # store this level

        return ans