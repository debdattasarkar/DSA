from collections import deque
class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
		"""
        BFS from the unique source over passable cells (1/2/3) looking for destination (2).

        Time:  O(n^2)   - each cell enqueued/dequeued at most once, 4 neighbors checked per cell.
        Space: O(n^2)   - 'visited' + queue in worst case.
        """
        n = len(grid)
        if n == 0:
            return 0  # no grid
        
        # 1) Locate source (and optionally destination) ------------------ O(n^2)
        src = None
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    src = (r, c)
                    break
            if src:
                break
        
        if not src:
            return 0  # no source found (shouldn't happen per constraints)
        
        # 2) Standard BFS setup ------------------------------------------ O(1)
        q = deque([src])
        visited = [[False] * n for _ in range(n)]
        visited[src[0]][src[1]] = True
        
        # 4-directional movement
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # 3) BFS loop ----------------------------------------------------- O(n^2)
        while q:
            r, c = q.popleft()  # Dequeue in O(1)
            
            # If we reached destination, return 1 in O(1)
            if grid[r][c] == 2:
                return 1
            
            # Explore 4 neighbors (bounded constant factor)
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # Boundary + wall + visited checks in O(1)
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))
        
        # Queue exhausted without hitting destination
        return 0