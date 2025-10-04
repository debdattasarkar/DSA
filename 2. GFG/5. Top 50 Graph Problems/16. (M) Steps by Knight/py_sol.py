from collections import deque

class Solution:
	def minStepToReachTarget(self, knightPos, targetPos, n):
		"""
        Classic BFS on an unweighted grid graph.
        - State: (r, c)
        - Start: knightPos
        - Goal:  targetPos
        - Edges: 8 knight moves inside [1..n] × [1..n]
        
        Time  : O(n^2) in worst case (every cell visited once)
        Space : O(n^2) for visited + queue
        """
        sr, sc = knightPos
        tr, tc = targetPos
        
        # Trivial case
        if (sr, sc) == (tr, tc):
            return 0
        
        # 8 knight moves
        moves = [(+1, +2), (+1, -2), (-1, +2), (-1, -2),
                 (+2, +1), (+2, -1), (-2, +1), (-2, -1)]
        
        # visited as a boolean grid (1-based indexing convenient here)
        visited = [[False] * (n + 1) for _ in range(n + 1)]
        q = deque()
        q.append((sr, sc, 0))      # (row, col, steps)
        visited[sr][sc] = True
        
        while q:
            r, c, d = q.popleft()
            # expand neighbors
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 1 <= nr <= n and 1 <= nc <= n and not visited[nr][nc]:
                    if (nr, nc) == (tr, tc):
                        return d + 1
                    visited[nr][nc] = True
                    q.append((nr, nc, d + 1))
        
        # For completeness; a knight on a finite board always reaches any square.
        return -1