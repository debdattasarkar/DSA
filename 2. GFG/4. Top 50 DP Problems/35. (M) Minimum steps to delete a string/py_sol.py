#User function Template for python3
class Solution:
	def minStepToDeleteString(self, s):
		n = len(s)
        if n == 0:
            return 0

        # dp[i][j] = min steps to delete s[i..j]
        dp = [[0] * n for _ in range(n)]

        # length 1 substrings -> 1 step
        for i in range(n):
            dp[i][i] = 1

        # length 2 substrings
        for i in range(n - 1):
            dp[i][i + 1] = 1 if s[i] == s[i + 1] else 2

        # length >= 3
        for length in range(3, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1

                best = float('inf')

                # Option 1: if ends equal, plan to remove both ends together
                # after clearing the middle (so no extra +1 here)
                if s[i] == s[j]:
                    best = min(best, dp[i + 1][j - 1])

                # Option 2: split into two parts and sum
                for k in range(i, j):
                    best = min(best, dp[i][k] + dp[k + 1][j])

                dp[i][j] = best

        return dp[0][n - 1]