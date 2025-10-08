#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    # Tarjan's algorithm for articulation points
    def articulationPoints(self, V, adj):
        tin  = [-1] * V     # discovery time
        low  = [0]  * V     # low-link value
        seen = [False] * V
        timer = 0
        is_ap = [False] * V  # articulation point flags

        def dfs(u: int, parent: int):
            nonlocal timer
            seen[u] = True
            tin[u]  = low[u] = timer
            timer  += 1

            children = 0  # number of DFS tree children

            for v in adj[u]:
                if v == parent:
                    continue
                if seen[v]:
                    # back edge: update low[u] with discovery time of v
                    low[u] = min(low[u], tin[v])
                else:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    # articulation condition for non-root
                    if parent != -1 and low[v] >= tin[u]:
                        is_ap[u] = True

                    children += 1

            # root is articulation iff it has >= 2 DFS children
            if parent == -1 and children >= 2:
                is_ap[u] = True

        # run DFS from all unvisited vertices (graph may be disconnected)
        for u in range(V):
            if not seen[u]:
                dfs(u, -1)

        ans = [i for i, ap in enumerate(is_ap) if ap]
        return ans if ans else [-1]