from collections import deque

class Solution:
    def numIslands(self, grid):
        """
        Flood-fill with DFS in 8 directions.
        Time  : O(n*m)  — each cell visited at most once
        Space : O(n*m)  — recursion stack in worst case + visited/marking
        """
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])

        # normalize to characters; if input is 0/1 you can tweak the check below
        def is_land(i, j):
            return grid[i][j] == 'L' or grid[i][j] == 1

        # 8 directions (dr, dc)
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]

        visited = [[False]*m for _ in range(n)]

        def dfs(r, c):
            # mark this cell O(1)
            visited[r][c] = True
            # explore 8 neighbors O(1) per neighbor
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and is_land(nr, nc):
                    dfs(nr, nc)

        islands = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and is_land(i, j):
                    islands += 1
                    dfs(i, j)      # flood-fill this island
        return islands