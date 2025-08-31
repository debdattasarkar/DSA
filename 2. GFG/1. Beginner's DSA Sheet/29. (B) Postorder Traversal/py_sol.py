'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return a list containing the postorder traversal of the tree.
    def postOrder(self, root):
        # code here
        # Left -> Right -> Root
        out = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)          # visit left subtree
            dfs(node.right)         # visit right subtree
            out.append(node.data)   # visit node
        dfs(root)
        return out