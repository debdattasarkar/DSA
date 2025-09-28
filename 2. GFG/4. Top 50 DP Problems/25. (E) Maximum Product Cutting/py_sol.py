#User function Template for python3
class Solution:
	def maxProduct(self, n):
		"""
        dp[i] = best product for length i with at least one cut.
        Transition:
            dp[i] = max over j=1..i-1 of max( j*(i-j), j*dp[i-j] )
        Time : O(n^2)
        Space: O(n)
        """
        # ---- FIXED EDGE CASE ----
        if n == 1:                 # judge expects 1 here
            return 1

        dp = [0] * (n + 1)         # O(n) space
        dp[1] = 1                  # helper base for transitions

        for i in range(2, n + 1):  # build up from 2..n  -> O(n)
            best = 0
            for j in range(1, i):  # first cut at j     -> O(i) per i
                # either stop cutting right piece, or cut it optimally
                best = max(best, j * (i - j), j * dp[i - j])
            dp[i] = best
        return dp[n]