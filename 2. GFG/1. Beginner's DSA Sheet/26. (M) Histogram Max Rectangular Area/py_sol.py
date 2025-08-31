
class Solution:
    def getMaxArea(self,arr):
        #code here
        """
        Monotonic increasing stack of indices.
        When current height < height[stack.top], pop and compute area where
        the popped bar is the limiting height; right boundary is current index,
        left boundary is the new stack.top (or -1 if empty).
        Time: O(n), each index pushed/popped once.
        Space: O(n) for the stack.
        """
        n = len(arr)
        st = []
        best = 0

        # process all bars, then a sentinel 0 to flush the stack
        for i in range(n + 1):
            cur = arr[i] if i < n else 0  # sentinel height 0 at the end
            # maintain increasing stack
            while st and cur < arr[st[-1]]:
                h = arr[st.pop()]
                left = st[-1] if st else -1  # index of previous smaller
                width = i - left - 1         # span where h is the min
                best = max(best, h * width)
            st.append(i)
        return best