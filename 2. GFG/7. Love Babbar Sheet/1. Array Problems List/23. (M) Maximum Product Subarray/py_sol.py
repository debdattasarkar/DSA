class Solution:
	def maxProduct(self,arr):
		"""
        Kadane-style for product:
        Keep max/min products ending at current index.
        Time : O(n)  (single pass)
        Space: O(1)  (constant extra variables)
        """
        if not arr:
            return 0  # or raise

        max_end = min_end = ans = arr[0]

        for x in arr[1:]:
            if x < 0:
                # Negative flips roles: what used to be min may become max
                max_end, min_end = min_end, max_end

            # Extend or restart at x
            max_end = max(x, max_end * x)
            min_end = min(x, min_end * x)

            # Track the best seen so far
            ans = max(ans, max_end)

        return ans