class Solution:
    def isBridge(self, V, edges, c, d):
        """
        Returns 1 if edge (c,d) is a bridge else 0.

        Core idea: Run a single DFS computing tin[u] (discovery time)
        and low[u] (lowest reachable discovery time). For tree edge (u->v),
        it's a bridge iff low[v] > tin[u].

        Time  : O(V + E)
        Space : O(V + E) for adjacency + O(V) for DFS stacks/arrays
        """
        # Normalize query edge as an unordered pair
        x, y = (c, d) if c <= d else (d, c)

        # Build adjacency + count parallel edges
        adj = [[] for _ in range(V)]
        multiplicity = {}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            a, b = (u, v) if u <= v else (v, u)
            multiplicity[(a, b)] = multiplicity.get((a, b), 0) + 1

        # If there are multiple edges between (c,d), removing one won't disconnect -> not a bridge
        if multiplicity.get((x, y), 0) > 1:
            return 0

        # Tarjan arrays
        tin  = [-1] * V   # discovery time
        low  = [-1] * V   # lowest discovery reachable
        timer = [0]
        seen_bridge = [False]  # flag to early stop when we find (c,d)

        import sys
        sys.setrecursionlimit(1_000_000)

        def dfs(u: int, parent: int):
            if seen_bridge[0]:
                return
            tin[u] = low[u] = timer[0]
            timer[0] += 1

            for v in adj[u]:
                if v == parent:
                    continue
                if tin[v] != -1:
                    # back edge
                    low[u] = min(low[u], tin[v])
                else:
                    # tree edge
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    # Check bridge condition for tree edge (u, v)
                    if low[v] > tin[u]:
                        # Is THIS the queried edge?
                        a, b = (u, v) if u <= v else (v, u)
                        if (a, b) == (x, y):
                            seen_bridge[0] = True
                            return

        # Graph may be disconnected; run DFS from every unvisited node
        for i in range(V):
            if tin[i] == -1:
                dfs(i, -1)
                if seen_bridge[0]:
                    break

        return 1 if seen_bridge[0] else 0