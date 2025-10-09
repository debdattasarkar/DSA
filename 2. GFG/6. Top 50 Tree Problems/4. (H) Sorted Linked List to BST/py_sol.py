#User function Template for python3

'''
#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
#Tree Node        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None
'''

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None

        # Helper: return (mid_prev, mid) where mid is middle node of list starting at head
        def find_mid(start):
            prev = None
            slow = fast = start
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            return prev, slow  # prev can be None if only 1 node

        # Base cases handled inside recursion
        def build(start):
            if not start:
                return None
            mid_prev, mid = find_mid(start)

            # mid is root
            root = TNode(mid.data)

            # left list is start .. mid_prev
            if mid_prev:
                mid_prev.next = None       # cut
                root.left = build(start)   # left from start to mid_prev
                mid_prev.next = mid        # (optional) restore if needed
            else:
                root.left = None

            # right list is mid.next .. end
            root.right = build(mid.next)
            return root

        return build(head)