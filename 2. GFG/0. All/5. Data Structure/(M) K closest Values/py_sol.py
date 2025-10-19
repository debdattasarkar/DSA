'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getKClosest(self, root, target, k):
        """
        Inorder → flat sorted list → pick k by (|diff|, value).
        Time  : O(n) to traverse + O(n log n) to sort by key
        Space : O(n) for values
        """
        vals = []
        self._inorder(root, vals)              # O(n)

        # Sort by primary key = |v-target|, secondary = v (smaller first on ties)
        vals.sort(key=lambda v: (abs(v - target), v))   # O(n log n)

        return vals[:k]                         # driver prints sorted anyway

    def _inorder(self, node, out):
        if not node: return
        self._inorder(node.left, out)
        out.append(node.data)
        self._inorder(node.right, out)
        
    