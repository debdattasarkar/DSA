class Solution: 
    def chocolatePickup(self, mat): 
        """
        Two-walker DP (cherry-pick style)
        Time:  O(n^3) states  (r1 in [0..n-1], c1 in [0..n-1], c2 in [0..n-1])
        Space: O(n^3) memo + O(n) recursion stack
        """
        from functools import lru_cache
        n = len(mat)

        @lru_cache(maxsize=None)
        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2  # ensure same step for walker2

            # invalid states
            if r1 < 0 or c1 < 0 or c2 < 0 or r2 < 0: return float('-inf')
            if r1 >= n or c1 >= n or c2 >= n or r2 >= n: return float('-inf')
            if mat[r1][c1] == -1 or mat[r2][c2] == -1:   return float('-inf')

            # destination
            if r1 == c1 == r2 == c2 == n - 1:
                return mat[n - 1][n - 1]

            gain = mat[r1][c1]
            if (r1, c1) != (r2, c2):
                gain += mat[r2][c2]

            # explore 4 combinations (R/D for each walker)
            best_next = max(
                dp(r1 + 1, c1,     c2    ),  # D, D
                dp(r1 + 1, c1,     c2 + 1),  # D, R
                dp(r1,     c1 + 1, c2    ),  # R, D
                dp(r1,     c1 + 1, c2 + 1)   # R, R
            )
            return gain + best_next

        ans = dp(0, 0, 0)
        return 0 if ans == float('-inf') else ans