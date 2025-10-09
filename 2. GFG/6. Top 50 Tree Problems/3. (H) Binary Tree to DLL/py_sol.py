'''
class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None
'''
class Solution:
    def bToDLL(self,root):
        if not root:
            return None

        stack = []
        curr = root
        head = prev = None

        # Standard iterative inorder traversal
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            node = stack.pop()  # inorder "visit"

            if prev is None:
                head = node
            else:
                prev.right = node
                node.left = prev
            prev = node

            curr = node.right

        return head