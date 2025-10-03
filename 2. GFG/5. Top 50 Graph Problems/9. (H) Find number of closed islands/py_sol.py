#User function Template for python3
from collections import deque
class Solution:
	def closedIslands(self, matrix, N, M):
		"""
        Approach: Flood-fill all land that touches the border; then count the
        remaining land components (those are closed).

        Let n=N, m=M.
        Time : O(n*m)  - each cell visited at most once across all BFS runs
        Space: O(n*m)  - visited + queue worst case
        """
        n, m = N, M
        if n == 0 or m == 0:
            return 0

        visited = [[False] * m for _ in range(n)]
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            visited[sr][sc] = True
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and matrix[nr][nc] == 1:
                        visited[nr][nc] = True
                        q.append((nr, nc))

        # 1) Remove/open all border-connected land ------------------ O(n*m)
        # Top & bottom rows
        for c in range(m):
            if matrix[0][c] == 1 and not visited[0][c]:
                bfs(0, c)
            if matrix[n-1][c] == 1 and not visited[n-1][c]:
                bfs(n-1, c)
        # Left & right columns
        for r in range(n):
            if matrix[r][0] == 1 and not visited[r][0]:
                bfs(r, 0)
            if matrix[r][m-1] == 1 and not visited[r][m-1]:
                bfs(r, m-1)

        # 2) Count closed islands among the remaining land ---------- O(n*m)
        count = 0
        for r in range(1, n-1):          # interior only is enough, but whole scan is fine
            for c in range(1, m-1):
                if matrix[r][c] == 1 and not visited[r][c]:
                    bfs(r, c)            # mark this closed component
                    count += 1

        return count