"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # Time: O(n) — visit each node once
        # Space: O(1) — constant extra pointers
        prev = None
        cur = head
        while cur:
            nxt = cur.next        # 1) save next      — O(1)
            cur.next = prev       # 2) reverse link   — O(1)
            prev = cur            # 3) advance prev   — O(1)
            cur = nxt             # 4) advance cur    — O(1)
        return prev               # prev is new head