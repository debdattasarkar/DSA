'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def mergeSort(self, head):
        """
        Top-down merge sort on a singly linked list.
        Time:  O(n log n)
        Space: O(log n) recursion stack (pointer work is O(1))
        """
        if not head or not head.next:             # base case 0/1 node
            return head

        # 1) split by middle
        mid = self._get_mid(head)                 # left end's middle
        right = mid.next
        mid.next = None                           # break into [head..mid], [right..]

        # 2) sort halves
        left_sorted = self.mergeSort(head)
        right_sorted = self.mergeSort(right)

        # 3) merge sorted halves
        return self._merge(left_sorted, right_sorted)

    def _get_mid(self, head):
        """Return node at end of left half (slow/fast)."""
        slow, fast = head, head.next
        # fast starts at head.next so mid becomes the left-middle for even length
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, a, b):
        """Merge two sorted lists a & b, return head. O(len(a)+len(b)) time, O(1) extra."""
        dummy = Node(0)
        tail = dummy
        while a and b:
            if a.data <= b.data:                 # stability: take from 'a' when equal
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a if a else b                # append remainder
        return dummy.next
        