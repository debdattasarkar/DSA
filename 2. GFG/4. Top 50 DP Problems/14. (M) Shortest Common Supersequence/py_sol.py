#User function Template for python3

class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, s1, s2):
        n, m = len(s1), len(s2)
        # dp[i][j] = SCS length for s1[:i] and s2[:j]
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        # base cases: one string empty → need all chars from the other
        for i in range(1, n+1):
            dp[i][0] = i
        for j in range(1, m+1):
            dp[0][j] = j
        
        # fill table
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        
        return dp[n][m]