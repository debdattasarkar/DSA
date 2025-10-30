class Solution:
    def fill(self, grid):
        """
        Mark border-connected 'O' as SAFE via DFS, flip the rest.
        Time  : O(n*m)  -- each cell visited at most once
        Space : O(n*m)  -- recursion stack worst-case + grid in-place
        """
        if not grid or not grid[0]:
            return grid

        rows, cols = len(grid), len(grid[0])

        # 4-directional moves
        DIRS = ((1,0), (-1,0), (0,1), (0,-1))

        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):
            # Mark this 'O' as SAFE ('S') to avoid flipping later
            grid[r][c] = 'S'
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if in_bounds(nr, nc) and grid[nr][nc] == 'O':
                    dfs(nr, nc)

        # 1) Seed DFS from all border 'O's
        for r in range(rows):
            if grid[r][0] == 'O': dfs(r, 0)
            if grid[r][cols-1] == 'O': dfs(r, cols-1)
        for c in range(cols):
            if grid[0][c] == 'O': dfs(0, c)
            if grid[rows-1][c] == 'O': dfs(rows-1, c)

        # 2) Flip interior 'O' -> 'X'
        # 3) Restore SAFE 'S' -> 'O'
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'   # surrounded
                elif grid[r][c] == 'S':
                    grid[r][c] = 'O'   # safe

        return grid