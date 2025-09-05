'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        """
        Floyd's tortoise-hare to detect a loop; if found, count its length.
        Time:  O(n)     (each pointer advances O(n) times)
        Space: O(1)     (constant extra pointers)
        """
        slow = fast = head

        # 1) Detect meeting point inside loop (if any)
        while fast and fast.next:
            slow = slow.next          # +1
            fast = fast.next.next     # +2
            if slow is fast:          # loop detected
                # 2) Count nodes in the loop: one full cycle from meeting point
                cnt = 1
                cur = slow.next
                while cur is not slow:
                    cnt += 1
                    cur = cur.next
                return cnt

        # No loop
        return 0