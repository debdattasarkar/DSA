
class Solution:
    def maximumAmount(self, arr):
        """
        dp[i][j] = max value current player can collect from arr[i..j]
        Recurrence:
          dp[i][j] = max(
              arr[i] + min(dp[i+2][j],   dp[i+1][j-1]),
              arr[j] + min(dp[i+1][j-1], dp[i][j-2])
          )
        Base:
          dp[i][i]   = arr[i]
          dp[i][i+1] = max(arr[i], arr[i+1])
        Time : O(n^2)  (n gaps, ~n cells per gap)
        Space: O(n^2)  table
        """
        n = len(arr)
        if n == 0:
            return 0  # not in constraints, safety

        dp = [[0]*n for _ in range(n)]

        # length 1
        for i in range(n):
            dp[i][i] = arr[i]

        # length 2
        for i in range(n-1):
            dp[i][i+1] = max(arr[i], arr[i+1])

        # lengths >= 3
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                # safe fetch with 0 when indices cross
                x = dp[i+2][j]   if i + 2 <= j else 0
                y = dp[i+1][j-1] if i + 1 <= j - 1 else 0
                z = dp[i][j-2]   if i <= j - 2 else 0

                pick_i = arr[i] + min(x, y)
                pick_j = arr[j] + min(y, z)
                dp[i][j] = max(pick_i, pick_j)

        return dp[0][n-1]