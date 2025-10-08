class Solution:
	def floodFill(self, image, sr, sc, newColor):
		"""
        DFS over the 4-connected component starting at (sr, sc).
        Time:  O(n * m)   -- each pixel visited at most once
        Space: O(n * m)   -- recursion stack in worst case (snakelike region)
        """
        n, m = len(image), len(image[0])
        old = image[sr][sc]
        if old == newColor:               # Important guard to avoid infinite recursion
            return image

        def dfs(r, c):
            # boundary and color check: O(1)
            if r < 0 or r >= n or c < 0 or c >= m or image[r][c] != old:
                return
            image[r][c] = newColor        # paint
            # explore 4 neighbors: O(1) each
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image