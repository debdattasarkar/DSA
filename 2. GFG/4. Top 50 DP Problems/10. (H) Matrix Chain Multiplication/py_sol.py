from functools import lru_cache

class Solution:
    def matrixMultiplication(self, arr):
        """
        Classic MCM with recursion + memo.
        Time  : O(n^3)  -- states O(n^2), each tries O(n) splits
        Space : O(n^2)  -- memo; recursion depth O(n)
        """
        n = len(arr) - 1
        if n <= 1:
            return 0

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0
            best = float("inf")
            # try all k as the final split
            for k in range(i, j):
                best = min(best,
                           dp(i, k) + dp(k + 1, j) + arr[i - 1] * arr[k] * arr[j])
            return best

        return dp(1, n)