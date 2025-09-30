#User function Template for python3
from functools import lru_cache
class Solution:
	def countWays(self, digits):
		# Time: O(n). Space: O(n) memo + O(n) stack.
        n = len(digits)

        @lru_cache(maxsize=None)
        def rec(i: int) -> int:
            if i == n:
                return 1
            if digits[i] == '0':
                return 0
            ways = rec(i + 1)  # single char
            if i + 1 < n and (digits[i] == '1' or
                               (digits[i] == '2' and '0' <= digits[i+1] <= '6')):
                ways += rec(i + 2)  # two chars
            return ways

        return rec(0)