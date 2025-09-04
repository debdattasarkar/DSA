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
        Reverse the list in groups of size k; the last (short) group is also reversed.
        Time:  O(n)   — each node is visited and rewired once
        Space: O(1)   — in-place pointer rewiring
        """
        if head is None or k <= 1:
            return head

        def reverse_chunk(start, k):
            """
            Reverse up to k nodes starting at 'start'.
            Returns (new_head, new_tail, next_start)
              - new_head: head of the reversed chunk
              - new_tail: tail of the reversed chunk (original 'start')
              - next_start: node after the chunk before reversal
            """
            prev, curr = None, start
            cnt = 0
            while curr is not None and cnt < k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                cnt += 1
            # prev is new_head of chunk; start is new_tail; curr is next_start
            return prev, start, curr

        dummy = Node(0)
        dummy.next = head
        prev_tail = dummy       # tail of the previous processed chunk
        curr = head

        while curr:
            new_head, new_tail, next_start = reverse_chunk(curr, k)

            # splice the reversed chunk into the main list
            prev_tail.next = new_head
            new_tail.next = next_start

            # advance
            prev_tail = new_tail
            curr = next_start

        return dummy.next