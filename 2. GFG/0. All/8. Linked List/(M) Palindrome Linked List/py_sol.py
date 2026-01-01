'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # Edge cases
        if head is None or head.next is None:
            return True

        # ---------- Helper: reverse a linked list ----------
        # Time: O(L), Space: O(1)
        def reverse_list(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # ---------- Step 1: Find middle using slow/fast ----------
        # Time: O(n), Space: O(1)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # If odd length, skip the middle element
        # Example: 1->2->3->2->1 (slow at 3; skip it)
        if fast is not None:
            slow = slow.next

        # ---------- Step 2: Reverse second half ----------
        # Time: O(n), Space: O(1)
        second_half_head = reverse_list(slow)

        # ---------- Step 3: Compare halves ----------
        # Time: O(n), Space: O(1)
        first_ptr = head
        second_ptr = second_half_head
        is_palindrome = True

        while second_ptr:  # only need to compare second half length
            if first_ptr.data != second_ptr.data:
                is_palindrome = False
                break
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next

        # ---------- Step 4 (optional): Restore list ----------
        # Time: O(n), Space: O(1)
        reverse_list(second_half_head)

        return is_palindrome