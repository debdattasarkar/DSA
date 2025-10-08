class Solution:

    #Function to find unit area of the largest region of 1s.
	def findMaxArea(self, grid):
		n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        # 8 directions: N, NE, E, SE, S, SW, W, NW
        dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                (1, 0), (1, -1), (0, -1), (-1, -1)]

        def inside(r, c):
            return 0 <= r < n and 0 <= c < m

        def dfs_area(sr, sc):
            """Flood-fill from (sr, sc) using a stack.
            Time per component: O(size_of_component)
            Space: O(size_of_component) for stack + visited (global O(n*m)).
            """
            stack = [(sr, sc)]
            visited[sr][sc] = True
            area = 0
            while stack:
                r, c = stack.pop()
                area += 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if inside(nr, nc) and not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        stack.append((nr, nc))
            return area

        max_area = 0
        # Overall Time: O(n*m) (each cell visited at most once)
        # Overall Space: O(n*m) for visited; stack worst-case O(n*m).
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, dfs_area(i, j))
        return max_area
