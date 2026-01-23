class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        prev_ge = [-1] * n   # previous index with arr[idx] >= arr[i]
        next_ge = [n] * n    # next index with arr[idx] >= arr[i]

        # -------- prev greater-or-equal (>=) using decreasing stack --------
        # Stack stores indices with heights in NON-increasing order.
        stack = []
        for i in range(n):
            # pop strictly smaller, because they can't block current or future >= queries
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            prev_ge[i] = stack[-1] if stack else -1
            stack.append(i)

        # -------- next greater-or-equal (>=) from right --------
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            next_ge[i] = stack[-1] if stack else n
            stack.append(i)

        # visible[i] = next_ge[i] - prev_ge[i] - 1
        best = 1
        for i in range(n):
            visible = next_ge[i] - prev_ge[i] - 1
            if visible > best:
                best = visible

        return best