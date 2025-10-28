class Solution:
	def nearest(self, grid):
		"""
        Multi-source BFS from all ones.
        Steps:
          1) Enqueue every cell with value 1 with distance 0.
          2) BFS to fill neighbors' distance if not set yet.
        Time  : O(n*m)  -- each cell enters queue at most once
        Space : O(n*m)  -- for dist/queue
        """
        n, m = len(grid), len(grid[0])

        # Initialize distances with +inf; set 0 where grid==1 and enqueue those cells
        dist = [[float('inf')] * m for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))   # multi-source seed

        # 4-connected directions
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        # Standard BFS
        while q:
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # in-bounds and can we relax to a shorter distance?
                if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        return dist