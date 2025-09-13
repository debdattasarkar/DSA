class Solution:
    def spirallyTraverse(self, mat):
        """
        Layer-by-layer traversal using four shrinking boundaries.

        Time:  O(n * m) — each cell is visited once
        Space: O(1)     — ignoring the result array we must return
        """
        if not mat or not mat[0]:
            return []

        n, m = len(mat), len(mat[0])
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        res = []

        while top <= bottom and left <= right:
            # 1) left -> right on the top row
            for j in range(left, right + 1):
                res.append(mat[top][j])
            top += 1

            # 2) top -> bottom on the right column
            for i in range(top, bottom + 1):
                res.append(mat[i][right])
            right -= 1

            # 3) right -> left on the bottom row (if still valid)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(mat[bottom][j])
                bottom -= 1

            # 4) bottom -> top on the left column (if still valid)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(mat[i][left])
                left += 1

        return res