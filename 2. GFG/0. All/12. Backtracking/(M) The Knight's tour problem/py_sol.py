class Solution:
    def knightTour(self, n):
        """
        Returns:
          - n x n matrix with visit order (0..n^2-1) if a tour exists,
          - [[-1]] if no tour exists (to satisfy the driver that checks for 1x1 [-1]).

        Notes:
          • Tours exist for n = 1 and for all n ≥ 5 (classical result).
          • No tour for n ∈ {2,3,4}.
          • Uses Warnsdorff’s heuristic (backtracking) for speed.
        """
        # Driver expects [[-1]] for impossible — do NOT return integer -1.
        if n in (2, 3, 4):
            return [[-1]]
        if n == 1:
            return [[0]]

        # Knight moves
        MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                 (-2, -1), (-1, -2), (1, -2), (2, -1)]

        board = [[-1]*n for _ in range(n)]
        board[0][0] = 0  # start at (0,0)

        def inside(x, y):
            return 0 <= x < n and 0 <= y < n

        def onward_degree(x, y):
            """How many unvisited moves from (x,y)? (used by Warnsdorff)"""
            c = 0
            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy
                if inside(nx, ny) and board[nx][ny] == -1:
                    c += 1
            return c

        def next_moves(x, y):
            """Warnsdorff ordering: fewest onward moves first; deterministic tiebreak."""
            cand = []
            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy
                if inside(nx, ny) and board[nx][ny] == -1:
                    cand.append((onward_degree(nx, ny), nx, ny))
            cand.sort()
            for _, nx, ny in cand:
                yield nx, ny

        def dfs(step, x, y):
            if step == n*n - 1:
                return True
            for nx, ny in next_moves(x, y):
                board[nx][ny] = step + 1
                if dfs(step + 1, nx, ny):
                    return True
                board[nx][ny] = -1  # backtrack
            return False

        # Run search; if it fails (shouldn’t for n≥5 from (0,0), but be safe), return [[-1]]
        return board if dfs(0, 0, 0) else [[-1]]