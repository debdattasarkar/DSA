from functools import lru_cache
class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPS(self,s):
        # Time: O(n^2) unique (i,j) states. Space: O(n^2) memo + O(n) recursion.
        n = len(s)

        @lru_cache(None)
        def dp(i, j):
            if i > j:  # empty range has 0 pal subsequences
                return 0
            if i == j:  # single char
                return 1
            if s[i] == s[j]:
                # dp(i+1,j) + dp(i,j-1) + 1
                return dp(i + 1, j) + dp(i, j - 1) + 1
            else:
                # inclusion-exclusion
                return dp(i + 1, j) + dp(i, j - 1) - dp(i + 1, j - 1)

            # Note: no modulo needed here (n ≤ 30); add % MOD if required by judge.

        return dp(0, n - 1)