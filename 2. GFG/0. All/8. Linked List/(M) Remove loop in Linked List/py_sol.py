
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val


class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        if not head or not head.next:
            return

        slow = head
        fast = head

        # Step 1: Detect loop using Floyd’s algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return  # No loop

        # Step 2: Find the start of the loop
        slow = head
        if slow == fast:
            # Special case: loop starts at head
            while fast.next != slow:
                fast = fast.next
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

        # Step 3: Break the loop
        fast.next = None