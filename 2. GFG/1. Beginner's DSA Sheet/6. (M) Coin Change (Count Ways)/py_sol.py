class Solution:
    def count(self, coins, target_sum):
        # Number of coins
        n = len(coins)

        # Step 1: Initialize DP array
        dp = [0] * (target_sum + 1)
        dp[0] = 1  # Base case: One way to make sum 0

        # Step 2: Iterate over each coin
        for coin in coins:
            for i in range(coin, target_sum + 1):
                dp[i] += dp[i - coin]  # Add ways to make (i - coin)

        return dp[target_sum]
