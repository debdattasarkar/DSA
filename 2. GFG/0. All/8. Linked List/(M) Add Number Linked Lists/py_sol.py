'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def addTwoLists(self, head1, head2):
        # ---------- Helper: reverse a linked list ----------
        # Time: O(L), Space: O(1)
        def reverse_list(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # ---------- Helper: remove leading zeros ----------
        # Time: O(L), Space: O(1)
        def strip_leading_zeros(head):
            # Keep at least one node if the number is 0
            while head and head.data == 0 and head.next:
                head = head.next
            return head

        # 1) Reverse both input lists (in-place)
        # Time: O(n+m), Space: O(1)
        rev1 = reverse_list(head1)
        rev2 = reverse_list(head2)

        # 2) Add digit-by-digit like classic addition
        # Time: O(n+m), Space: O(1) extra (output list nodes are required)
        carry = 0
        dummy = Node(0)
        tail = dummy

        ptr1, ptr2 = rev1, rev2
        while ptr1 or ptr2 or carry:
            digit1 = ptr1.data if ptr1 else 0
            digit2 = ptr2.data if ptr2 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10

            tail.next = Node(digit)
            tail = tail.next

            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next

        # 3) Reverse the result to restore forward order
        # Time: O(n+m), Space: O(1)
        result = reverse_list(dummy.next)

        # 4) Remove leading zeros in output
        result = strip_leading_zeros(result)

        # (Optional) If you want to restore input lists to original order, reverse rev1/rev2 back.
        return result