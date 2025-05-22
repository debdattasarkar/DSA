class Solution:
    def minDeletions(self,s):
        # code here 
        n = len(s)
        rev = s[::-1]  # reverse the string

        # dp[i][j] = LCS of s[0:i] and rev[0:j]
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # minimum deletions = total length - LPS length
        return n - dp[n][n]
