from collections import deque

class Solution:
    def reverseQueue(self, q):
        """
        Reverse the queue in-place using a stack.
        Works for both list (used as a queue) and collections.deque.

        Time  : O(n)
        Space : O(n)   # the stack
        """
        # Is it a deque (has popleft)? Otherwise assume list with pop(0)
        is_deque = hasattr(q, "popleft")
        stack = []

        # 1) Dequeue everything to the stack
        while q:
            # pop from front (queue semantics)
            x = q.popleft() if is_deque else q.pop(0)
            stack.append(x)

        # 2) Pop from stack and enqueue back (reverses order)
        while stack:
            q.append(stack.pop())

        return q