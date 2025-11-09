class Solution:
    def spirallyTraverse(self, mat):
        """
        Boundary 'peel the onion' approach.
        Time:  O(n*m)  (each cell visited once)
        Space: O(1)    (aside from output)
        """
        if not mat or not mat[0]:
            return []

        n, m = len(mat), len(mat[0])
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        result = []

        while top <= bottom and left <= right:
            # 1) Left -> Right on current top row
            for col in range(left, right + 1):
                result.append(mat[top][col])
            top += 1

            # 2) Top -> Bottom on current right column
            for row in range(top, bottom + 1):
                result.append(mat[row][right])
            right -= 1

            # 3) Right -> Left on current bottom row (guard to avoid re-traversal)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(mat[bottom][col])
                bottom -= 1

            # 4) Bottom -> Top on current left column (guard again)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(mat[row][left])
                left += 1

        return result