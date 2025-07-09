class Solution:
    def sumSubMins(self, arr):
        n = len(arr)
        mod = 10**9 + 7

        # Step 1: Initialize Previous and Next Less Element arrays
        # Time: O(n)
        ple = [-1] * n   # PLE[i]: index of previous less element
        nle = [n] * n    # NLE[i]: index of next less element
        stack = []

        # Step 2: Compute Previous Less Element (PLE)
        # Time: O(n), each element is pushed/popped once
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            ple[i] = stack[-1] if stack else -1
            stack.append(i)

        # Clear stack for NLE computation
        stack.clear()

        # Step 3: Compute Next Less Element (NLE)
        # Time: O(n), same as PLE
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nle[i] = stack[-1] if stack else n
            stack.append(i)

        # Step 4: Compute final result using contribution of each element
        # Time: O(n)
        result = 0
        for i in range(n):
            left = i - ple[i]       # Elements to the left where arr[i] is min
            right = nle[i] - i      # Elements to the right where arr[i] is min
            result += arr[i] * left * right
            result %= mod           # To avoid overflow

        return result