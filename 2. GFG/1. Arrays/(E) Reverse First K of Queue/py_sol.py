from queue import Queue

class Solution:
    def modifyQueue(self, q, k):
        # Step 1: Use stack to reverse first k elements
        stack = []
        for _ in range(k):
            stack.append(q.get())  # O(k)

        # Step 2: Enqueue stack elements back into queue
        while stack:
            q.put(stack.pop())  # O(k)

        # Step 3: Move the remaining (size-k) elements to the rear
        size = q.qsize()
        for _ in range(size - k):
            q.put(q.get())  # O(n-k)

        return q