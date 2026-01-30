from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        half = n // 2
        stack = []

        # Step 1: push first half into stack
        # Time: O(n/2), Space: O(n/2)
        for _ in range(half):
            stack.append(q.popleft())

        # Step 2: push stack back to queue (reversed first half goes behind)
        # Time: O(n/2)
        while stack:
            q.append(stack.pop())

        # Step 3: rotate first half (now at front) to back to restore order separation
        # Time: O(n/2)
        for _ in range(half):
            q.append(q.popleft())

        # Step 4: again push first half (original order now at front) into stack
        # Time: O(n/2)
        for _ in range(half):
            stack.append(q.popleft())

        # Step 5: interleave stack (first half) + queue (second half)
        # stack top is the correct next element of first half
        # Time: O(n)
        while stack:
            q.append(stack.pop())    # element from first half
            q.append(q.popleft())    # element from second half

        return q