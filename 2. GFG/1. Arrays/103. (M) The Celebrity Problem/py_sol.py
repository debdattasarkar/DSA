class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        a, b = 0, n - 1

        # Step 1: Elimination
        while a < b:
            if mat[a][b] == 1:
                a += 1  # a knows b → a is not celebrity
            else:
                b -= 1  # a does not know b → b is not celebrity

        candidate = a

        # Step 2: Verification
        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1
        return candidate