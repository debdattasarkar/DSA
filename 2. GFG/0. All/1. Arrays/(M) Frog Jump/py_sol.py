
class Solution:
    def minCost(self, height):
        """
        Time:  O(n)   (single pass)
        Space: O(1)   (keep only two previous dp values)
        """
        n = len(height)
        if n <= 1:
            return 0

        # dp[0] = 0, dp[1] = |h1 - h0|
        prev2 = 0
        prev1 = abs(height[1] - height[0])

        for i in range(2, n):
            cost1 = prev1 + abs(height[i] - height[i - 1])  # jump from i-1
            cost2 = prev2 + abs(height[i] - height[i - 2])  # jump from i-2
            curr = cost1 if cost1 < cost2 else cost2
            prev2, prev1 = prev1, curr  # slide window

        return prev1