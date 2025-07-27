class Solution:
    def balanceSums(self, mat):
        # code here
        n = len(mat)  # since it's a square matrix

        # Step 1: Compute row and column sums
        rowSum = [0] * n
        colSum = [0] * n

        for i in range(n):
            for j in range(n):
                rowSum[i] += mat[i][j]
                colSum[j] += mat[i][j]

        # Step 2: Determine the maximum row/column sum (target sum)
        maxSum = max(max(rowSum), max(colSum))

        # Step 3: Traverse each cell and adjust towards maxSum
        i = j = 0
        ops = 0

        while i < n and j < n:
            # Determine minimum increment we can apply at (i, j)
            diff = min(maxSum - rowSum[i], maxSum - colSum[j])
            mat[i][j] += diff
            rowSum[i] += diff
            colSum[j] += diff
            ops += diff  # count operations

            # Move to next row/col that needs work
            if rowSum[i] == maxSum:
                i += 1
            if colSum[j] == maxSum:
                j += 1

        return ops