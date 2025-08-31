'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self,root):
        # code here
        # Time:  O(n) -- each node visited once
        # Space: O(h) -- recursion stack height (h = tree height; O(n) worst, O(log n) best)
        ans = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)          # 1) left
            ans.append(node.data)   # 2) node
            dfs(node.right)         # 3) right

        dfs(root)
        return ans
