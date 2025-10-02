#User function Template for python3
from collections import deque
class Solution:
    def fill(self,  mat):
        """
        Mark border-connected 'O' as safe via multi-source BFS, then flip others.
        
        Let n = rows, m = cols.
        Time:  O(n*m)    # each cell enqueued/visited at most once
        Space: O(n*m)    # worst-case queue; in-place marker uses O(1) extra
        """
        if not mat or not mat[0]:
            return mat
        
        n, m = len(mat), len(mat[0])
        q = deque()
        
        # 1) Push all border 'O' cells into the queue (multi-source BFS).
        # Top & bottom rows
        for c in range(m):
            if mat[0][c] == 'O':
                q.append((0, c))
                mat[0][c] = '#'           # mark safe in-place (O(1) space)
            if mat[n-1][c] == 'O':
                q.append((n-1, c))
                mat[n-1][c] = '#'
        # Left & right columns
        for r in range(n):
            if mat[r][0] == 'O':
                q.append((r, 0))
                mat[r][0] = '#'
            if mat[r][m-1] == 'O':
                q.append((r, m-1))
                mat[r][m-1] = '#'
        
        # 2) BFS: mark every 'O' reachable from border as '#'
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:                            # each cell visited at most once -> total O(n*m)
            r, c = q.popleft()
            for dr, dc in DIRS:             # constant 4 neighbors
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 'O':
                    mat[nr][nc] = '#'
                    q.append((nr, nc))
        
        # 3) Final pass: flip unmarked 'O' to 'X', restore '#' to 'O'
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 'O':        # not safe -> surrounded -> flip
                    mat[r][c] = 'X'
                elif mat[r][c] == '#':      # safe -> restore
                    mat[r][c] = 'O'
        
        return mat