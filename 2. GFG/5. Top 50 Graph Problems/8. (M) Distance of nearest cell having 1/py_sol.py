from collections import deque

class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		"""
        Multi-source BFS seeded with all '1' cells.
        Let n = rows, m = cols.

        Time : O(n*m)    each cell enqueued/dequeued at most once
        Space: O(n*m)    for the queue + distance matrix
        """
        n, m = len(grid), len(grid[0])
        dist = [[-1] * m for _ in range(n)]       # -1 means unvisited
        q = deque()

        # Seed BFS with all 1-cells at distance 0  ---------------- O(n*m)
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        # 4-directional moves
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS ------------------------------------------------------ O(n*m)
        while q:
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # If not visited, set dist and enqueue
                if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        return dist