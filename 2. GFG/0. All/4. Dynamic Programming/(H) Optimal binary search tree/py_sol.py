from functools import lru_cache
class Solution:
    def minCost(self, keys, freq):
        """
        Top-down DP with memoization for Optimal BST.

        Time  : O(n^3)   (n^2 states * O(n) roots per state)
        Space : O(n^2)   for memo table + O(n) recursion stack
        """
        n = len(keys)
        if n == 0:
            return 0

        # Precompute prefix sums of frequencies:
        # prefixFreq[i] = sum of freq[0..i-1]
        prefixFreq = [0] * (n + 1)
        for i in range(n):
            prefixFreq[i + 1] = prefixFreq[i] + freq[i]

        def range_sum(i, j):
            """Return sum of freq[i..j] in O(1)."""
            if i > j:
                return 0
            return prefixFreq[j + 1] - prefixFreq[i]

        @lru_cache(maxsize=None)
        def solve(i, j):
            """
            Minimum cost for optimal BST using keys[i..j],
            assuming root of this subtree is at level 1.
            """
            if i > j:
                return 0
            if i == j:
                return freq[i]  # single node at level 1

            total_freq = range_sum(i, j)
            best = float('inf')

            # Try each key[i..j] as root
            for r in range(i, j + 1):
                left_cost = solve(i, r - 1)
                right_cost = solve(r + 1, j)
                cost = left_cost + right_cost + total_freq
                if cost < best:
                    best = cost

            return best

        return solve(0, n - 1)