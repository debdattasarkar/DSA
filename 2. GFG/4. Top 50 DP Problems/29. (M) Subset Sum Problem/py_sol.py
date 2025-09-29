class Solution:
    def isSubsetSum (self, arr, sum):
        """
        Iterative 0/1 subset-sum with O(sum) space.
        dp[t] = True if some subset makes total t.
        Time:  O(n * sum)
        Space: O(sum)
        """
        dp = [False] * (sum + 1)
        dp[0] = True  # base

        for x in arr:
            # iterate backward so each x is used at most once
            for t in range(sum, x - 1, -1):
                if dp[t - x]:
                    dp[t] = True
            # Optional early exit:
            if dp[sum]:
                return True

        return dp[sum]