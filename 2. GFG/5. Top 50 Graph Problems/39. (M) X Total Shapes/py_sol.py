class Solution:    
    #Function to find the number of 'X' total shapes.
	def xShape(self, grid):
		if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        visited = [[False]*m for _ in range(n)]
        
        # 4-directional moves (no diagonals)
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c):
            # Mark (r,c) as visited and expand to 4-neighbors that are 'X'
            visited[r][c] = True
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if grid[nr][nc] == 'X' and not visited[nr][nc]:
                        dfs(nr, nc)
        
        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 'X' and not visited[r][c]:
                    count += 1        # new component found
                    dfs(r, c)         # flood-fill the entire shape
        return count