'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class BST:
    def search(self, node, x):
        #code here
        # Optimized iterative: O(h) time, O(1) space
        cur = node
        while cur:
            if x == cur.data:
                return True
            elif x < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return False