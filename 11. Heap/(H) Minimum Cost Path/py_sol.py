import heapq

class Solution:
    
    #Function to return the minimum cost to react at bottom
	#right cell from top left cell.
	def minimumCostPath(self, grid):
		#Code here
		n = len(grid)
        min_heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while min_heap:
            cost, x, y = heapq.heappop(min_heap)
            if x == n - 1 and y == n - 1:
                return cost
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(min_heap, (cost + grid[nx][ny], nx, ny))