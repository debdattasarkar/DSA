class Solution:
    def countSquare(self, mat, x):
        # 2D Prefix Sum approach
        # Time: O(n*m) to build prefix + O(n*m*min(n,m)) to count squares
        # Space: O(n*m)

        n = len(mat)
        m = len(mat[0])
        max_size = min(n, m)

        # Build prefix sum array with extra row+col of zeros
        # prefix[r+1][c+1] stores sum of mat[0..r][0..c]
        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        # Build prefix
        # Time: O(n*m), Space already allocated
        for r in range(n):
            row_running = 0
            for c in range(m):
                row_running += mat[r][c]
                prefix[r + 1][c + 1] = prefix[r][c + 1] + row_running

        # Helper to get sum of rectangle in O(1)
        def rect_sum(r1, c1, r2, c2):
            # sum of mat[r1..r2][c1..c2] inclusive
            return (prefix[r2 + 1][c2 + 1]
                    - prefix[r1][c2 + 1]
                    - prefix[r2 + 1][c1]
                    + prefix[r1][c1])

        # Count all kxk squares
        # Time: O(n*m*min(n,m))
        count = 0
        for size in range(1, max_size + 1):
            for top_row in range(0, n - size + 1):
                bottom_row = top_row + size - 1
                for left_col in range(0, m - size + 1):
                    right_col = left_col + size - 1
                    if rect_sum(top_row, left_col, bottom_row, right_col) == x:
                        count += 1

        return count