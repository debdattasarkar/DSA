class Solution:
    def minCutCost(self, n, cuts):
        """
        Interval DP (memoized).
        Time:  O(m^3) in worst case  (m = len(cuts))
        Space: O(m^2) memo + O(m) recursion
        """
        pts = [0] + sorted(cuts) + [n]
        m = len(pts)

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            if j == i + 1:
                return 0
            best = float('inf')
            length = pts[j] - pts[i]
            # try first cut at every inner point
            for k in range(i + 1, j):
                best = min(best, length + dp(i, k) + dp(k, j))
            return best

        return dp(0, m - 1)