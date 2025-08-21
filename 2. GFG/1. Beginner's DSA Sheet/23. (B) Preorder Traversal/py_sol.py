'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def preorder(self,root):
        # code here
        if not root:
            return []
        
        ans, st = [], [root]
        while st:
            node = st.pop()            # pop current
            ans.append(node.data)      # visit Root
            # push Right first so Left is processed first
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return ans