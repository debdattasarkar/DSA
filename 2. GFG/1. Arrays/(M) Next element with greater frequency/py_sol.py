from collections import Counter
class Solution:
    def findGreater(self, arr):
        # code here

        n = len(arr)

        # Step 1: Count frequencies of each element
        # Time: O(n)
        # Space: O(n) for frequency map
        freq = Counter(arr)

        # Step 2: Initialize result with -1 (default)
        # Time: O(n)
        # Space: O(n) for result array
        result = [-1] * n

        # Step 3: Monotonic Stack to track indices
        # Time: Overall O(n), each index is pushed/popped once
        # Space: O(n) for the stack
        stack = []

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            # Pop stack while frequency at top is <= current
            while stack and freq[arr[stack[-1]]] <= freq[arr[i]]:
                stack.pop()

            # If stack not empty, top is the next greater frequency element
            if stack:
                result[i] = arr[stack[-1]]

            # Push current index to stack for future use
            stack.append(i)

        return result

