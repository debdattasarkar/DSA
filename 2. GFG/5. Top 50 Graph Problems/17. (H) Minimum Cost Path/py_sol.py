import heapq
from math import inf

class Solution:
    
    # Function to return the minimum cost to react at bottom
    # right cell from top left cell.
    def minimumCostPath(self, grid):
        n = len(grid)                           # O(1)
        # dist[r][c] = best known cost to reach (r, c)
        dist = [[inf] * n for _ in range(n)]    # O(n^2) space & init time
        dist[0][0] = grid[0][0]                 # cost includes start cell
        
        # Min-heap of (current_cost, r, c)
        pq = [(grid[0][0], 0, 0)]               # O(1) push
        # 4-direction moves
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Dijkstra: each cell can be popped at most once with its final cost
        # Time: each push/pop is O(log (n^2)) = O(log n). Total O(n^2 log n).
        while pq:
            cost, r, c = heapq.heappop(pq)      # O(log n)
            # If we popped a stale pair (greater than best), skip in O(1)
            if cost != dist[r][c]:
                continue
            # Early exit: first time we pop target -> optimal
            if r == n - 1 and c == n - 1:
                return cost                      # O(1)
            # Relax 4 neighbors
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n: # O(1)
                    ncost = cost + grid[nr][nc] # pay neighbor cell cost
                    if ncost < dist[nr][nc]:    # strict improvement
                        dist[nr][nc] = ncost
                        heapq.heappush(pq, (ncost, nr, nc))  # O(log n)

        # Should never get here since grid is connected via 4-dir moves
        return dist[n-1][n-1]