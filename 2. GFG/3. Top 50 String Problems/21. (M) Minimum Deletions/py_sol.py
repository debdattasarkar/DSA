class Solution:
    def minDeletions(self,s):
        """
        Bottom-up DP for LPS.
        Time : O(n^2)
        Space: O(n^2)  (can be optimized to O(n) with rolling rows/diagonals)
        """
        n = len(s)
        if n <= 1:
            return 0

        dp = [[0] * n for _ in range(n)]
        # single chars are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # length from 2..n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        lps = dp[0][n - 1]
        return n - lps