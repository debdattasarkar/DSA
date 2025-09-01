'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        # code here
        """
        Swaps the k-th node from start with k-th from end (1-based).
        Time:  O(n)  (single pass to get length + two short scans)
        Space: O(1)
        """
        if head is None:
            return head

        # 1) Compute length n
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # 2) If k out of range or same node -> no change
        if k < 1 or k > n:
            return head
        if k == n - k + 1:  # same node
            return head

        # Helper to fetch (prev, node) for the p-th node from start (1-based)
        def get_prev_and_node(head, p):
            prev = None
            cur = head
            for _ in range(p - 1):
                prev = cur
                cur = cur.next
            return prev, cur

        # 3) Identify both nodes (and their prevs)
        prev1, node1 = get_prev_and_node(head, k)
        prev2, node2 = get_prev_and_node(head, n - k + 1)

        # 4) Handle adjacency explicitly (two cases)
        if node1.next is node2:  # node1 immediately before node2
            if prev1: prev1.next = node2
            else:     head = node2
            node1.next = node2.next
            node2.next = node1
            return head

        if node2.next is node1:  # node2 immediately before node1
            if prev2: prev2.next = node1
            else:     head = node1
            node2.next = node1.next
            node1.next = node2
            return head

        # 5) Non-adjacent: swap links via prev1/prev2 and swap next pointers
        if prev1: prev1.next = node2
        else:     head = node2
        if prev2: prev2.next = node1
        else:     head = node1

        node1.next, node2.next = node2.next, node1.next
        return head
