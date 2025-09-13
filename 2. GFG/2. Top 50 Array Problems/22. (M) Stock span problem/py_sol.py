class Solution:
    def calculateSpan(self, arr):
        """
        Monotonic stack of indices storing a strictly decreasing sequence of prices.
        For day i: pop indices with price <= arr[i] so the new top (if any) is the
        previous greater element (PGE). Span = i - PGE_index (or i - (-1) if none).
        
        Time:  O(n) total — each index is pushed once and popped at most once
        Space: O(n) for the stack + O(n) for the output
        """
        n = len(arr)
        span = [0] * n
        st = []  # stack of indices, prices strictly decreasing along the stack

        for i in range(n):
            # Pop while current price dominates (<= because equal prices also extend span)
            while st and arr[st[-1]] <= arr[i]:
                st.pop()

            prev_greater_idx = st[-1] if st else -1
            span[i] = i - prev_greater_idx

            st.append(i)   # push current index to serve as PGE for future days

        return span