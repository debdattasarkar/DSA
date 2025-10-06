'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from collections import deque
class Solution:
    def bottomView(self, root):
        """
        Level-order (BFS) + horizontal distance.
        Time  : O(n)  — each node enqueued/dequeued once; final sort by distinct hd (≤ n)
        Space : O(n)  — queue + map
        """
        if not root:
            return []

        # Queue holds (node, hd)
        q = deque([(root, 0)])
        hd_to_val = {}  # {hd: node.data}

        while q:
            node, hd = q.popleft()

            # For bottom view, we want the last (lowest) node seen at each hd in BFS order.
            # Overwrite is intentional: latter nodes in level order replace earlier ones.
            hd_to_val[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))

        # Collect values by increasing horizontal distance
        result = [hd_to_val[hd] for hd in sorted(hd_to_val.keys())]
        return result
        