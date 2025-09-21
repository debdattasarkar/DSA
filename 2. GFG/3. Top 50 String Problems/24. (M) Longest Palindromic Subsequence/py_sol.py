#User function Template for python3

class Solution:

    def longestPalinSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # length 1 substrings are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # build by increasing substring length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1] if n else 0