#User function Template for python3
class Solution:
	def maxSubstring(self, S):
		"""
        Map '0' -> +1, '1' -> -1 and run Kadane to get the max subarray sum.
        If the best sum <= 0 (e.g., all '1's), return -1.
        Time  : O(n)  -- one pass
        Space : O(1)  -- constant extra space
        """
        best = 0           # best sum found so far
        cur = 0            # current subarray sum

        for ch in S:
            val = 1 if ch == '0' else -1
            # Either start new at val or extend previous (Kadane)
            cur = max(val, cur + val)
            best = max(best, cur)

        return best if best > 0 else -1