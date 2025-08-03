class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        rows, cols = len(mat), len(mat[0])
        row0 = col0 = False

        # Step 1: Mark rows and columns
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    if i == 0:
                        row0 = True
                    if j == 0:
                        col0 = True
                    mat[i][0] = 0
                    mat[0][j] = 0

        # Step 2: Update the matrix using the markers
        for i in range(1, rows):
            for j in range(1, cols):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0

        # Step 3: Handle first row
        if row0:
            for j in range(cols):
                mat[0][j] = 0

        # Step 4: Handle first column
        if col0:
            for i in range(rows):
                mat[i][0] = 0

        return mat