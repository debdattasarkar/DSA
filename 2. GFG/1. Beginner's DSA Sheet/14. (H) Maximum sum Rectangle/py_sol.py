class Solution:
    def maxRectSum(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])

        max_sum = float('-inf')

        # Loop over all pairs of rows
        for top in range(n):
            temp = [0] * m
            for bottom in range(top, n):

                # Add current row to the temp array (column-wise sum)
                for col in range(m):
                    temp[col] += mat[bottom][col]

                # Apply Kadane's Algorithm on temp
                curr_sum = temp[0]
                max_ending_here = temp[0]

                for i in range(1, m):
                    max_ending_here = max(temp[i], max_ending_here + temp[i])
                    curr_sum = max(curr_sum, max_ending_here)

                max_sum = max(max_sum, curr_sum)

        return max_sum