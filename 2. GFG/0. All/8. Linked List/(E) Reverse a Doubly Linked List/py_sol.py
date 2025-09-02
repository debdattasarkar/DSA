"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        """
        Reverse a doubly linked list by swapping next/prev at each node.
        - Time:  O(n)  (touch each node once)
        - Space: O(1)  (in-place)

        Steps:
          1) Walk curr from head to tail.
          2) For each curr: swap curr.next and curr.prev.
          3) After swap, move curr = curr.prev  (because links swapped).
          4) Track 'new_head' as the last node processed.
        """
        curr = head
        new_head = None
        while curr:
            # swap pointers
            curr.prev, curr.next = curr.next, curr.prev
            # record potential new head
            new_head = curr
            # move forward in the *reversed* sense
            curr = curr.prev
        return new_head
        