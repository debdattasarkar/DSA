from typing import List
class Solution:
    def prefixSum2D(self, mat, queries):
        """
        Optimized solution using a 2D prefix sum array.

        Steps:
            1. Precompute prefix sums:
                   pref[i][j] = sum of mat[x][y] for 0 <= x <= i, 0 <= y <= j
               Using recurrence:
                   pref[i][j] = mat[i][j]
                                + (pref[i-1][j]   if i > 0 else 0)
                                + (pref[i][j-1]   if j > 0 else 0)
                                - (pref[i-1][j-1] if i > 0 and j > 0 else 0)

            2. For each query [r1, c1, r2, c2], compute:
                   total = pref[r2][c2]
                           - (pref[r1-1][c2]   if r1 > 0 else 0)
                           - (pref[r2][c1-1]   if c1 > 0 else 0)
                           + (pref[r1-1][c1-1] if r1 > 0 and c1 > 0 else 0)

        Complexity:
            Let n = number of rows, m = number of columns, q = number of queries.

            Building pref: O(n * m)
            Answering queries: O(q) (each is O(1))
            -> Total Time: O(n * m + q)
            Auxiliary Space: O(n * m) for pref.
                (If we overwrite mat with prefix sums, extra space can be O(1).)
        """
        n = len(mat)
        if n == 0:
            return []
        m = len(mat[0])

        # 1) Build 2D prefix sum matrix 'pref'
        pref = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                top = pref[i - 1][j] if i > 0 else 0
                left = pref[i][j - 1] if j > 0 else 0
                diag = pref[i - 1][j - 1] if i > 0 and j > 0 else 0
                pref[i][j] = mat[i][j] + top + left - diag

        # 2) Answer each query in O(1) using the prefix sums.
        answers: List[int] = []
        for r1, c1, r2, c2 in queries:
            total = pref[r2][c2]

            if r1 > 0:
                total -= pref[r1 - 1][c2]
            if c1 > 0:
                total -= pref[r2][c1 - 1]
            if r1 > 0 and c1 > 0:
                total += pref[r1 - 1][c1 - 1]

            answers.append(total)

        return answers