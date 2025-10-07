class Solution:
    
    def topoSort(self, V, edges):
        # Step 1: Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        
        visited = [False] * V
        stack = []

        # Step 2: DFS utility
        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            # Post-order insertion
            stack.append(node)
        
        # Step 3: Call DFS on all unvisited nodes
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        # Step 4: Reverse stack to get topological order
        return stack[::-1]