class Solution:
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)

        # Step 1: Initialize result array with -1
        # Time: O(n)
        res = [-1] * n

        # Step 2: Stack to store indices of next greater candidates
        # Space: O(n) in worst case
        stack = []

        # Step 3: Traverse the array in reverse (2n - 1 to 0)
        # to simulate circular array behavior
        # Time: O(2n) = O(n), each element pushed/popped at most once
        for i in range(2 * n - 1, -1, -1):
            cur = arr[i % n]

            # Pop smaller/equal elements from the stack
            while stack and arr[stack[-1]] <= cur:
                stack.pop()

            # Fill result only in the first n indices
            if i < n:
                if stack:
                    res[i] = arr[stack[-1]]
                # If no greater element found, result[i] remains -1

            # Push current index modulo n to stack
            stack.append(i % n)

        return res