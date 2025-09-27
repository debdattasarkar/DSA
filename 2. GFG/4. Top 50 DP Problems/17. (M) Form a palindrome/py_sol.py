from functools import lru_cache

class Solution:
    def findMinInsertions(self, s):
        n = len(s)

        @lru_cache(maxsize=None)
        def solve(i: int, j: int) -> int:
            # States: O(n^2)
            if i >= j:
                return 0
            if s[i] == s[j]:
                return solve(i + 1, j - 1)         # reuse overlapping subproblems
            return 1 + min(solve(i + 1, j), solve(i, j - 1))

        # Time: O(n^2) unique (i,j) pairs; each computed once.
        # Space: O(n^2) for cache + recursion stack O(n).
        return solve(0, n - 1)