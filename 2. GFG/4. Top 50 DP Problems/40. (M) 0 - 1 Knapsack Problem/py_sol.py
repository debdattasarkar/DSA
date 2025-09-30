class Solution:
    def knapsack(self, W, val, wt):
        """
        0-1 Knapsack (capacity as DP dimension).
        Time:  O(n * W) – n items, each updates up to W capacities.
        Space: O(W)     – single array dp[0..W].

        dp[w] = best value with capacity <= w using processed items.
        Backward capacity loop ensures each item is used at most once.
        """
        n = len(val)
        dp = [0] * (W + 1)  # O(W) space

        for i in range(n):                   # O(n)
            wi, vi = wt[i], val[i]
            # iterate capacities backwards to avoid reusing item i
            for w in range(W, wi - 1, -1):   # O(W)
                dp[w] = max(dp[w], vi + dp[w - wi])

        return dp[W]