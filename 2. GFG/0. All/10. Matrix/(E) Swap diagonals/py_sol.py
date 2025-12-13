from typing import List
class Solution:
    def swapDiagonal(self, mat):
        """
        Optimized in-place solution.

        For each row i:
            - major diagonal index  = (i, i)
            - minor diagonal index  = (i, n-1-i)
            Swap mat[i][i] with mat[i][n-1-i].

        Because we only touch two cells per row:
            Time  : O(n)
            Space : O(1) extra (we modify mat in place).

        If n is odd, the middle cell (i == n//2) is on both diagonals.
        Our swap still works: we swap the cell with itself, no issue.
        """
        n = len(mat)
        if n == 0:
            return mat  # nothing to do

        for i in range(n):           # O(n) iterations
            j_major = i             # column of major diagonal
            j_minor = n - 1 - i     # column of minor diagonal

            # Swap values on the same row between the two diagonals
            mat[i][j_major], mat[i][j_minor] = mat[i][j_minor], mat[i][j_major]

        return mat