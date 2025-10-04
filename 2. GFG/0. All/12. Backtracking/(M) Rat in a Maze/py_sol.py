class Solution:
    def ratInMaze(self, maze):
        """
        Optimized backtracking: single 'visited' grid; mark before recursing, unmark after.
        Explore in order D,L,R,U to naturally emit lexicographically smallest paths.

        Time  : O(4^(n*n)) in worst-case enumeration (but very fast for n<=5)
        Space : O(n*n) for visited + O(n*n) recursion worst depth
        """
        n = len(maze)
        if n == 0 or maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return []

        res = []
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        # Ordered as 'D'<'L'<'R'<'U' to match lexicographic requirement
        dirs = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]

        def dfs(r, c, path):
            if r == n - 1 and c == n - 1:
                res.append(path)
                return
            for dr, dc, ch in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True          # mark
                    dfs(nr, nc, path + ch)
                    visited[nr][nc] = False         # unmark (backtrack)

        dfs(0, 0, "")
        # No need to sort if you preserved D,L,R,U order; sort() is harmless safety:
        # res.sort()
        return res