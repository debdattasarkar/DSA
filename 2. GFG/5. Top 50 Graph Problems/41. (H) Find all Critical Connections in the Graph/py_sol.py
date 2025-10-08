#User function Template for python3
class Solution:
    def criticalConnections(self, v, adj):
        """
        adj: adjacency list of an undirected graph with vertices [0..v-1]
        Return: list of [u, v] pairs (u < v) representing all bridges, sorted.
        """
        import sys
        sys.setrecursionlimit(10**6)

        time = 0
        disc = [-1] * v      # discovery time
        low  = [0]  * v      # low-link value
        parent = [-1] * v
        bridges = []

        def dfs(u):
            nonlocal time
            time += 1
            disc[u] = low[u] = time

            for w in adj[u]:
                if disc[w] == -1:         # tree edge
                    parent[w] = u
                    dfs(w)
                    low[u] = min(low[u], low[w])

                    # Bridge condition: no back-edge from w or its subtree
                    if low[w] > disc[u]:
                        bridges.append([min(u, w), max(u, w)])
                elif w != parent[u]:      # back edge
                    low[u] = min(low[u], disc[w])

        # Graph can be disconnected in some test setups; handle all components
        for u in range(v):
            if disc[u] == -1:
                dfs(u)

        # Sort output as required
        bridges.sort()
        return bridges