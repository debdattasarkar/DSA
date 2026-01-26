class Solution:
    def findWays(self, n):
        # Odd length cannot form balanced parentheses
        if n % 2 == 1:
            return 0

        pairs = n // 2

        # dp[i] = number of valid parentheses expressions with i pairs
        dp = [0] * (pairs + 1)
        dp[0] = 1  # one way to arrange 0 pairs: empty string

        for i in range(1, pairs + 1):
            ways = 0
            # split i pairs into: (inside has j pairs) + (outside has i-1-j pairs)
            for inside_pairs in range(i):
                outside_pairs = i - 1 - inside_pairs
                ways += dp[inside_pairs] * dp[outside_pairs]
            dp[i] = ways

        return dp[pairs]