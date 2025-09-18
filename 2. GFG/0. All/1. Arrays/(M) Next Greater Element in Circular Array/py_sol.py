class Solution:
    def nextGreater(self, arr):
        """
        Monotonic stack over two passes (simulate circular array):
        - Time : O(n)  (each index pushed and popped at most once)
        - Space: O(n)  (stack + output)
        """
        n = len(arr)
        ans = [-1] * n
        st = []  # stack of indices whose NGE we haven't found yet

        # Traverse twice; only push indices from the first pass
        for i in range(2 * n):
            j = i % n
            # Resolve as long as current value is greater than stack top
            while st and arr[j] > arr[st[-1]]:
                ans[st.pop()] = arr[j]
            # Push only during the first pass so each index is pushed once
            if i < n:
                st.append(j)
        return ans