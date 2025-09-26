#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        """
        DP definition:
          dp[j] = length of LCSuffix ending at current s1 char and s2[j-1]
        We keep only one row (rolling), and a 'prev' cell for dp[i-1][j-1].

        Time : O(n * m)  -- every pair (i,j) visited once
        Space: O(min(n, m))  -- we make the shorter string the columns
        """
        # Ensure s2 is the shorter to minimize space
        if len(s2) > len(s1):
            s1, s2 = s2, s1

        n, m = len(s1), len(s2)
        dp = [0] * (m + 1)      # dp[0]=0 is sentinel
        best = 0

        for i in range(1, n + 1):
            prev_diag = 0       # this holds dp[j-1] from previous row (dp[i-1][j-1])
            for j in range(1, m + 1):
                temp = dp[j]    # save current dp[j] before overwriting; it's dp[i-1][j]
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev_diag + 1
                    if dp[j] > best:
                        best = dp[j]
                else:
                    dp[j] = 0   # reset because substring must be contiguous
                prev_diag = temp
        return best