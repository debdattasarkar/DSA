#User function Template for python3
import math

class Solution:
	def MinSquares(self, n):
		"""
        Bottom-up DP:
          dp[x] = 1 + min_{s in squares, s<=x} dp[x - s]
        Time : O(n * sqrt(n))  -- ~sqrt(n) squares per x
        Space: O(n)
        """
        # Precompute all perfect squares ≤ n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        dp = [0] + [10**9] * n     # dp[0]=0, others large
        for x in range(1, n + 1):  # O(n)
            # Try every square ≤ x
            for s in squares:      # up to O(sqrt(n)) per x
                if s > x:
                    break
                dp[x] = min(dp[x], 1 + dp[x - s])
        return dp[n]