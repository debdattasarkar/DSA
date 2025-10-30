from collections import deque, defaultdict
from typing import List

class Solution:
    def shortCycle(self, V, edges):
        """
        BFS-from-each-vertex (most expected).
        Time  : O(V * (V + E))   -- fresh BFS per source
        Space : O(V + E)         -- adjacency + BFS arrays
        """
        # Build adjacency list: O(V + E)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        INF = 10**9
        best = INF

        # BFS from every node as source
        for s in range(V):
            # Fresh structures per BFS to avoid cross-contamination
            dist   = [-1] * V
            parent = [-1] * V
            q = deque([s])
            dist[s] = 0

            while q:
                u = q.popleft()
                for v in graph[u]:
                    if dist[v] == -1:
                        # Tree edge
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:
                        # Found a non-parent visited neighbor -> cycle
                        # Length = dist[u] + dist[v] + 1
                        cycle_len = dist[u] + dist[v] + 1
                        if cycle_len < best:
                            best = cycle_len
                # Optional micro-optimization: early stop if best==3
                # if best == 3: return 3

        return -1 if best == INF else best