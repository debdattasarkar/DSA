class Solution:

    def kosaraju(self, adj):
        #code here
        def dfs(v, visited, stack):
            visited[v] = True
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs(neighbor, visited, stack)
            stack.append(v)

        def reverse_graph():
            rev = [[] for _ in range(V)]
            for u in range(V):
                for v in adj[u]:
                    rev[v].append(u)
            return rev

        def dfs_reverse(v, visited, rev):
            visited[v] = True
            for neighbor in rev[v]:
                if not visited[neighbor]:
                    dfs_reverse(neighbor, visited, rev)

        # 1. First pass
        visited = [False] * V
        stack = []
        for i in range(V):
            if not visited[i]:
                dfs(i, visited, stack)

        # 2. Reverse the graph
        rev = reverse_graph()

        # 3. Second pass
        visited = [False] * V
        scc_count = 0
        while stack:
            node = stack.pop()
            if not visited[node]:
                dfs_reverse(node, visited, rev)
                scc_count += 1

        return scc_count