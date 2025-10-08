from collections import deque

class Solution:
	def orangesRotting(self, mat):
		"""
        Multi-source BFS from all initially rotten cells.
        - Each BFS layer = 1 minute.
        - Stop when no fresh left or queue exhausted.

        Let n = rows, m = cols.
        Time:  O(n*m)   - each cell enqueued at most once, 4 neighbors per cell (constant).
        Space: O(n*m)   - queue in worst case.
        """
        if not mat or not mat[0]:
            return 0

        n, m = len(mat), len(mat[0])
        q = deque()
        fresh = 0

        # 1) Collect all rotten (sources) and count fresh ---------- O(n*m)
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 2:
                    q.append((r, c))
                elif mat[r][c] == 1:
                    fresh += 1

        # No fresh oranges? Time = 0
        if fresh == 0:
            return 0

        minutes = 0
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        # 2) BFS layers while we still have fresh ------------------ ≤ O(n*m)
        while q and fresh > 0:
            for _ in range(len(q)):  # process one "minute" worth
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    # if neighbor is fresh, rot it and enqueue
                    if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                        mat[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1  # finished one minute of spread

        # 3) If fresh remains, impossible
        return minutes if fresh == 0 else -1