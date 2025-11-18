import heapq
class Solution:
    def minCostPath(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        # cost[r][c] := minimum possible path cost (minimized maximum diff)
        # to reach cell (r, c) from (0, 0)
        cost = [[float('inf')] * cols for _ in range(rows)]
        cost[0][0] = 0
        
        # Min-heap of (current_cost, row, col)
        min_heap = [(0, 0, 0)]
        
        # 4-directional movement
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while min_heap:
            current_cost, r, c = heapq.heappop(min_heap)
            
            # If this entry is outdated (we already found a better cost), skip it
            if current_cost > cost[r][c]:
                continue
            
            # If we reached the destination, current_cost is the answer
            if r == rows - 1 and c == cols - 1:
                return current_cost
            
            # Relax all 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Edge effort between current cell and neighbor
                    edge_diff = abs(mat[r][c] - mat[nr][nc])
                    
                    # If we go to neighbor through this path, the maximum difference
                    # on that path becomes max(current path cost, this edge's diff)
                    new_cost = max(current_cost, edge_diff)
                    
                    # Standard Dijkstra relaxation with our modified cost definition
                    if new_cost < cost[nr][nc]:
                        cost[nr][nc] = new_cost
                        heapq.heappush(min_heap, (new_cost, nr, nc))
        
        # For safety, though we should have returned earlier
        return cost[rows - 1][cols - 1]