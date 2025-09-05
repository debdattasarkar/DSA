'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        """
        Build 3 sublists (0, 1, 2) and concatenate.
        - Single pass to distribute nodes -> O(n)
        - Constant extra pointers          -> O(1) space
        - Stable: preserves relative order within each value
        """
        if head is None:
            return None
        
        # Dummy heads and tails for 0s, 1s, 2s
        zH = Node(-1); zT = zH   # zeros
        oH = Node(-1); oT = oH   # ones
        tH = Node(-1); tT = tH   # twos
        
        cur = head
        while cur:
            nxt = cur.next
            cur.next = None          # detach to avoid accidental cycles
            if cur.data == 0:
                zT.next = cur; zT = cur
            elif cur.data == 1:
                oT.next = cur; oT = cur
            else:
                tT.next = cur; tT = cur
            cur = nxt
        
        # Concatenate non-empty buckets in order 0 -> 1 -> 2
        # Start from first non-empty list
        new_head = None
        # link zeros to ones/twos
        if zH.next:
            new_head = zH.next
            zT.next = oH.next if oH.next else tH.next
        # link ones to twos
        if oH.next:
            if new_head is None:
                new_head = oH.next
            oT.next = tH.next
        # if only 2s exist
        if new_head is None:
            new_head = tH.next
        
        return new_head