'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMedian(self, root):
        """
        Two-pass Morris inorder (O(1) extra space):
          1) Count nodes n with Morris.
          2) Visit again and return k-th element in inorder (k per problem rule).
        Time  : O(n)
        Space : O(1) auxiliary (threads are created & restored)
        """

        if not root:
            return -1  # guard, though constraints imply at least 1 node

        # --- Pass 1: count nodes with Morris ---
        def count_nodes(node):
            count = 0
            curr = node
            while curr:
                if curr.left is None:
                    count += 1
                    curr = curr.right
                else:
                    # find inorder predecessor
                    pred = curr.left
                    while pred.right and pred.right is not curr:
                        pred = pred.right
                    if pred.right is None:
                        pred.right = curr       # thread
                        curr = curr.left
                    else:
                        pred.right = None       # unthread
                        count += 1
                        curr = curr.right
            return count

        n = count_nodes(root)

        # k: 1-indexed target per statement
        k = (n // 2) if (n % 2 == 0) else (n // 2 + 1)

        # --- Pass 2: return k-th value with Morris ---
        curr = root
        visited = 0
        while curr:
            if curr.left is None:
                visited += 1
                if visited == k:
                    return curr.data
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                if pred.right is None:
                    pred.right = curr           # thread
                    curr = curr.left
                else:
                    pred.right = None           # unthread
                    visited += 1
                    if visited == k:
                        return curr.data
                    curr = curr.right

        return -1  # should not happen with valid inputs