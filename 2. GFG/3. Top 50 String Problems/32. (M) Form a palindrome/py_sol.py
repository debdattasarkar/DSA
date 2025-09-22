#User function Template for python3

class Solution:
    def countMin(self, s):
        """
        dp[i][j] = min insertions to make s[i..j] a palindrome
        Time  : O(n^2)
        Space : O(n^2)
        """
        n = len(s)
        if n <= 1:
            return 0

        dp = [[0]*n for _ in range(n)]  # dp on intervals

        # iterate by increasing window length
        for length in range(2, n+1):
            for i in range(0, n-length+1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] if j - i > 1 else 0
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]