#User function Template for python3
from functools import lru_cache
class Solution:
	def TotalCount(self, s):
		"""
        F(i, last) = number of valid groupings for s[i:], given previous sum = last.
        Transition: choose any j >= i with cur=sum(i..j) and cur >= last, then add F(j+1, cur).
        Time:  O(N^3) in worst case (each state scans j and sums grow), N<=100 is fine.
        Space: O(N^2) for memo table (last in 0..9N) + O(N) recursion.
        """
        n = len(s)
        digits = [ord(c) - 48 for c in s]  # 0..9

        @lru_cache(maxsize=None)
        def F(i: int, last: int) -> int:
            if i == n:
                return 1  # one way to end
            ways = 0
            cur = 0
            for j in range(i, n):
                cur += digits[j]
                if cur >= last:              # non-decreasing group sums
                    ways += F(j + 1, cur)    # next state jumps to j+1
            return ways

        return F(0, 0)