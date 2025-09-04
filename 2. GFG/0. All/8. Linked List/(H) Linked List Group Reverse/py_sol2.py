"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        """
        Time:  O(n)
        Space: O(n) recursion stack in the worst case
        """
        if head is None or k <= 1:
            return head

        # reverse up to k nodes
        prev, curr = None, head
        cnt = 0
        while curr is not None and cnt < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            cnt += 1
        # 'prev' is new head of this reversed block, 'head' is new tail
        head.next = self.reverseKGroup(curr, k)
        return prev