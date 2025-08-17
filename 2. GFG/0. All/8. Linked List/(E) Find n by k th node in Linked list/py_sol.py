'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data   
        self.next = None
'''
        
class Solution:
    def fractional_node(self, head, k):
        """
        Returns value at ceil(n/k)-th node (1-based) using one pass.
        Time  : O(n)  — visit each node once
        Space : O(1)  — constant extra pointers
        """
        if head is None or k <= 0:
            return -1  # or None per platform

        frac = head          # will end at ceil(n/k)-th node
        cur = head
        i = 0

        # Walk with 'cur', bump 'frac' once after every k nodes
        # but only if we aren't at the final node (cur.next != None)
        while cur:
            i += 1
            if i % k == 0 and cur.next is not None:
                frac = frac.next
            cur = cur.next

        return frac.data