class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        candidate = 0

        # Step 1: Find a potential candidate
        for i in range(1, n):
            # If candidate knows i, they can't be celebrity
            if mat[candidate][i] == 1:
                candidate = i

        # Step 2: Validate candidate
        for i in range(n):
            if i != candidate:
                # Candidate should not know i, and everyone should know candidate
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1

        return candidate