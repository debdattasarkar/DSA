class Solution:
    def applyDiff2D(self, mat, opr):
        # code here 
        n, m = len(mat), len(mat[0])

        # Step 1: Create a difference matrix of size (n+2) x (m+2)
        diff = [[0] * (m + 2) for _ in range(n + 2)]

        # Step 2: Apply all operations to the difference matrix
        for v, r1, c1, r2, c2 in opr:
            diff[r1][c1] += v
            diff[r1][c2 + 1] -= v
            diff[r2 + 1][c1] -= v
            diff[r2 + 1][c2 + 1] += v

        # Step 3: Compute prefix sum over rows
        for i in range(n + 1):
            for j in range(1, m + 1):
                diff[i][j] += diff[i][j - 1]

        # Step 4: Compute prefix sum over columns
        for j in range(m + 1):
            for i in range(1, n + 1):
                diff[i][j] += diff[i - 1][j]

        # Step 5: Update the original matrix with final values
        for i in range(n):
            for j in range(m):
                mat[i][j] += diff[i][j]

        return mat