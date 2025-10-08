'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        # Recursive DFS: left -> right -> node
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)          # 1) traverse left subtree
            dfs(node.right)         # 2) traverse right subtree
            res.append(node.data)   # 3) visit node
        dfs(root)
        return res