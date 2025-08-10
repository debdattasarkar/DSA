class Solution:
    def transpose(self, mat):
        # code here
        """
        In-place transpose for a square matrix.
        Time:  O(n^2)  -- two nested loops over upper triangle
        Space: O(1)    -- swaps done in place
        """
        n = len(mat)                 # number of rows == number of cols (square)

        # swap only above the main diagonal (j > i)
        for i in range(n):           # O(n)
            for j in range(i + 1, n):  # O(n - i - 1) each row
                # swap mat[i][j] with mat[j][i]
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        return mat  # (some platforms expect in-place only; returning mat is convenien