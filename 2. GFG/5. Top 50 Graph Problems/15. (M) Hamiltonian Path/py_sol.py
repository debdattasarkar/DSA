#User function Template for python3
class Solution:
    def check(self, n, m, edges): 
        """
        Backtracking over path endpoints.
        Build adjacency list. For each start node, DFS picking unvisited neighbors.
        
        Time  : O(n! ) worst-case, but n ≤ 10 so it's fine; heavy pruning from adjacency.
        Space : O(n + m) for graph + O(n) recursion stack + O(n) visited.
        """
        # Build 0-based adjacency
        adj = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1; v -= 1
            adj[u].append(v)
            adj[v].append(u)

        # Quick pruning: if any isolated vertex and n>1 -> impossible
        if n > 1 and any(len(adj[i]) == 0 for i in range(n)):
            return 0

        visited = [False] * n

        def dfs(u, depth):
            """Return True if we can build a path of length 'depth' ending at u."""
            if depth == n:                      # visited all vertices exactly once
                return True
            # Try unvisited neighbors
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    if dfs(v, depth + 1):
                        return True
                    visited[v] = False
            return False

        # Try each vertex as a starting point
        for s in range(n):
            visited[s] = True
            if dfs(s, 1):
                return 1
            visited[s] = False
        return 0