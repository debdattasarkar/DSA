#User function Template for python3
class Solution:
    def maximumPath(self, mat):
        """
        DP by rows:
          curr[c] = mat[r][c] + max(prev[c-1], prev[c], prev[c+1])
        Keep only prev row -> O(m) space.

        Time : O(n*m)
        Space: O(m)
        """
        n = len(mat)
        m = len(mat[0]) if n else 0
        if n == 0 or m == 0:
            return 0

        prev = mat[0][:]                      # dp for row 0

        for r in range(1, n):
            curr = [0] * m
            for c in range(m):
                best_above = prev[c]
                if c > 0:
                    best_above = max(best_above, prev[c-1])
                if c+1 < m:
                    best_above = max(best_above, prev[c+1])
                curr[c] = mat[r][c] + best_above
            prev = curr                        # roll
        return max(prev)                       # best in last row