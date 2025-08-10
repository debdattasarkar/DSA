class Solution:
    def rotateMatrix(self, mat):
        # code here
        """
        Rotate square matrix `mat` by 90 degrees anti-clockwise, in-place.

        Steps:
        1) Transpose in-place (swap across main diagonal)
        2) Reverse each column in-place
        """
        n = len(mat)
        if n == 0: 
            return mat  # nothing to do

        # 1) Transpose
        for i in range(n):
            # j starts at i+1 to avoid swapping diagonal and double-swaps
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        # 2) Reverse each column
        for col in range(n):
            top, bottom = 0, n - 1
            while top < bottom:
                mat[top][col], mat[bottom][col] = mat[bottom][col], mat[top][col]
                top += 1
                bottom -= 1

        return mat