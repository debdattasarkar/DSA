#User function Template for python3
class Solution:
	def minDifference(self, arr):
		"""
        Bitset subset-sum DP.
        Time:  O(n * S / w)  (Python big-int shifts are efficient; in practice fast)
        Space: O(S) bits (bitset stored in a Python int)
        """
        S = sum(arr)
        bits = 1  # bit 0 set => sum 0 achievable
        for a in arr:
            # shift left by 'a' and OR: adds 'a' to all existing achievable sums
            bits |= (bits << a)

        # Look for the achievable sum t closest to S//2 (scan downward)
        half = S // 2
        # Check bits from half down to 0; the first set bit minimizes |S-2t|
        for t in range(half, -1, -1):
            if (bits >> t) & 1:
                return S - 2 * t