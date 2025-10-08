class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        V = len(adj)
        visited = [False] * V       # Track visited nodes
        result = []

        def dfs_util(v):
            visited[v] = True
            result.append(v)
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs_util(neighbor)

        dfs_util(0)  # Start DFS from node 0
        return result