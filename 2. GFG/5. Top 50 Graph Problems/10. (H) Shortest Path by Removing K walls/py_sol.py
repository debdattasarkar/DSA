#User function Template for python3
from collections import deque

class Solution:
    def shotestPath(self, mat, n, m, k):
        """
        BFS over state = (r, c, rem_k) with pruning by best remaining k per cell.

        Let N=n, M=m.
        Time  : O(N*M*K)    (each (r,c) can be improved up to K times)
        Space : O(N*M) for 'seen' + O(N*M) for queue in worst case
        """
        # Quick target check
        if n == 0 or m == 0:
            return -1
        if (n - 1, m - 1) == (0, 0):
            return 0  # already there

        # seen[r][c] = max remaining k we've ever had upon reaching (r,c)
        seen = [[-1] * m for _ in range(n)]
        q = deque()
        q.append((0, 0, k))
        seen[0][0] = k

        steps = 0
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            # process one BFS layer => one step
            for _ in range(len(q)):
                r, c, rem = q.popleft()

                if (r, c) == (n - 1, m - 1):
                    return steps

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m:
                        nrem = rem
                        if mat[nr][nc] == 1:
                            if rem == 0:      # can't remove more
                                continue
                            nrem = rem - 1    # consume a wall

                        # prune if we have seen this cell with >= remaining walls
                        if nrem <= seen[nr][nc]:
                            continue
                        seen[nr][nc] = nrem
                        q.append((nr, nc, nrem))
            steps += 1

        return -1