#User function Template for python3
class Solution:
    #Function to count paths between two vertices in a directed graph.
    def countPaths(self, V, adj, source, destination):
        # Brute-force DFS over all paths.
        # Time: O(#paths) worst-case can be O(V!) in dense DAGs
        # Space: O(V) recursion stack + pathVisited
        
        pathVisited = [False] * V  # guards against cycles / revisits in current path

        def dfs(u):
            # Reached destination => exactly one path
            if u == destination:
                return 1
            pathVisited[u] = True
            total = 0
            for v in adj[u]:
                # avoid revisiting the same node in current path (safe even if input is a DAG)
                if not pathVisited[v]:
                    total += dfs(v)
            pathVisited[u] = False  # backtrack
            return total

        return dfs(source)