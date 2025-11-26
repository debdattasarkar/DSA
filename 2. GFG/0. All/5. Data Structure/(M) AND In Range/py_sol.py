class Solution:
	def andInRange(self, l, r):
		"""
        Compute bitwise AND of all integers from l to r inclusive.

        Core idea:
        ----------
        - Over a continuous range, bits that flip (0→1 or 1→0) at any point
          become 0 in the final AND.
        - The only bits that survive are the leading bits where l and r
          have the SAME value (the common prefix).
        - We repeatedly right-shift l and r until they are equal, counting
          how many times we shifted. This removes the non-common suffix.
        - When l == r, that value is exactly the common prefix.
        - Shift it back left by 'shift' places (filling with zeroes) to get
          the final AND result.

        Time Complexity:
            O(log(max(l, r)))  -- we shift at most the bit-length times.
        Space Complexity:
            O(1)  -- just a few integer variables.
        """
        shift = 0

        # Keep trimming least-significant bits until l and r converge.
        # Each step:
        #   l >>= 1, r >>= 1  -> O(1)
        # Loop runs at most ~30 times for l,r <= 1e9.
        while l < r:
            l >>= 1
            r >>= 1
            shift += 1

        # l (or r) now holds the common prefix; restore zeros on the right.
        return l << shift