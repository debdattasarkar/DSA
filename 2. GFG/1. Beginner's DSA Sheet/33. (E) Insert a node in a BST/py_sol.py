'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def insert(self, root, key):
        # code here 
        """
        Time:  O(h) where h is the height of the BST
        Space: O(h) recursion stack
        """
        # Base: empty spot -> place new node here
        if root is None:
            return Node(key)

        if key < root.data:
            # Insert into left subtree and reattach (important for persistence)
            root.left = self.insert(root.left, key)
        elif key > root.data:
            # Insert into right subtree and reattach
            root.right = self.insert(root.right, key)
        else:
            # key == root.data: duplicate; do nothing
            return root

        return root