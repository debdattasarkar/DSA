class Solution:
    def mergeStones(self, stones, k):
        """
        Interval DP with memoization.
        Time  : O(n^3 / (k-1)) in practice (n<=30 fits)
        Space : O(n^2) memo
        """
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        # prefix sums for O(1) range sum
        pref = [0]
        for x in stones:
            pref.append(pref[-1] + x)
        def rng(i, j):  # sum of stones[i..j]
            return pref[j + 1] - pref[i]

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0
            best = float('inf')
            # Only split at steps of (k-1)
            m = i
            while m < j:
                best = min(best, dp(i, m) + dp(m + 1, j))
                m += (k - 1)
            # If we can compress current interval into 1 pile, pay its sum
            if (j - i) % (k - 1) == 0:
                best += rng(i, j)
            return best

        return dp(0, n - 1)