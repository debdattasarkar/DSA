#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        def dfs(node, visited):
            visited[node] = True
            for neighbor in range(V):
                # Check if connected and not visited
                if adj[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor, visited)

        visited = [False] * V
        count = 0

        # Run DFS for every unvisited node
        for i in range(V):
            if not visited[i]:
                count += 1
                dfs(i, visited)
        
        return count