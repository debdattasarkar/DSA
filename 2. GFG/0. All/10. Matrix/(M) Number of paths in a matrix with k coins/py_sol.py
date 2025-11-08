class Solution:
    def numberOfPath(self, mat, k):
        # code here
        n, m = len(mat), len(mat[0])

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def ways_from(i, j, remain):
            # Out of bounds
            if i >= n or j >= m:
                return 0
            val = mat[i][j]
            if remain < val:
                return 0
            # Destination cell
            if i == n - 1 and j == m - 1:
                return 1 if remain == val else 0

            remain2 = remain - val
            down  = ways_from(i + 1, j, remain2)
            right = ways_from(i, j + 1, remain2)
            return down + right

        return ways_from(0, 0, k)