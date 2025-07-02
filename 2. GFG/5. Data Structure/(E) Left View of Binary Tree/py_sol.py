
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None


#Function to return a list containing elements of left view of the binary tree.
class Solution:
    def LeftView(self, root):
        # code here
        if not root:
            return []
        
        result = []
        queue = [root]

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                if i == 0:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result