#User function Template for python3
from collections import deque
class Solution:
    # Function to find the level (shortest path length) from node 0 to X.
    # Time: O(V + E)  |  Space: O(V)
    def nodeLevel(self, V, adj, X):
        # Basic bounds check (cheap guard)
        if X < 0 or X >= V:
            return -1
        if X == 0:
            return 0
        
        dist = [-1] * V  # -1 = unvisited
        dist[0] = 0
        q = deque([0])
        
        while q:
            u = q.popleft()
            # Early exit if we've reached X
            if u == X:
                return dist[u]
            for v in adj[u]:
                if dist[v] == -1:     # not visited
                    dist[v] = dist[u] + 1
                    q.append(v)
        
        # If X wasn't reached
        return -1