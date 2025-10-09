#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    # Return a list containing the post order traversal of the given tree
    def postOrder(self,node):
        if not node:
            return []
        
        stack = []
        ans = []
        last = None   # last visited node
        curr = node
        
        while curr or stack:
            # push left spine
            while curr:
                stack.append(curr)
                curr = curr.left
            
            peek = stack[-1]
            # if right child exists and not processed yet, go right
            if peek.right and last is not peek.right:
                curr = peek.right
            else:
                # visit the node
                ans.append(peek.data)
                last = stack.pop()
                # loop continues with curr=None to consider parent
        return ans