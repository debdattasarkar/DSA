class Solution:
    def countPaths(self, edges, V, src, dest):
        #Code here
        from collections import defaultdict

        # Build graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        memo = [-1] * V  # dp[node] = number of paths from node to dest

        def dfs(node):
            if node == dest:
                return 1
            if memo[node] != -1:
                return memo[node]
            total = 0
            for neighbor in graph[node]:
                total += dfs(neighbor)
            memo[node] = total
            return total

        return dfs(src)