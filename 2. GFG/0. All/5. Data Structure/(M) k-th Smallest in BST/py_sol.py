'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthSmallest(self, root, k): 
        """
        Iterative inorder: walk to leftmost, then unwind with a stack.
        Each pop is the next-smallest value; when we pop the k-th time, return it.
        Time  : O(h + k)  (worst O(n))
        Space : O(h)      (stack)
        """
        stack = []
        current = root
        visited_count = 0

        # Standard inorder traversal
        while current or stack:
            # go as left as possible
            while current:
                stack.append(current)
                current = current.left

            # visit node
            current = stack.pop()
            visited_count += 1
            if visited_count == k:
                return current.data

            # then go right
            current = current.right

        return -1  # k larger than number of nodes