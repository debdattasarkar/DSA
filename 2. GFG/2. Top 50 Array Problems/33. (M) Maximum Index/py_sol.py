class Solution:
    def maxIndexDiff(self, arr):
        n = len(arr)
        if n <= 1:
            return 0

        # Step 1: strictly decreasing stack of indices
        st = []
        for i, x in enumerate(arr):
            if not st or arr[st[-1]] > x:
                st.append(i)

        # Step 2: scan from right; widen while arr[st[-1]] <= arr[j]
        best = 0
        for j in range(n-1, -1, -1):
            while st and arr[st[-1]] <= arr[j]:
                i = st.pop()
                best = max(best, j - i)
        return best