class Solution:
    def longestSubarray(self, arr):
        """
        For each index i, find nearest strictly-greater element on the left and right
        using two monotonic decreasing stacks. The maximal window where arr[i] is the
        maximum is (left[i]+1 .. right[i]-1) of length L_i. If arr[i] <= L_i, it's a
        valid candidate. Return the best L_i.

        Time  : O(n)   (each index pushed/popped at most once per pass)
        Space : O(n)
        """
        n = len(arr)
        if n == 0:
            return 0

        # nearest strictly-greater to the right, default n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                right[stack.pop()] = i
            stack.append(i)

        # nearest strictly-greater to the left, default -1
        left = [-1] * n
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                left[stack.pop()] = i
            stack.append(i)

        ans = 0
        for i in range(n):
            length = right[i] - left[i] - 1  # maximal span with arr[i] as max
            if arr[i] <= length:
                ans = max(ans, length)
        return ans