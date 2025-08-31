#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        """
        Standard Bellman–Ford (edge-relaxation) with negative-cycle detection.
        Time:  O(V * E)
        Space: O(V)
        Returns: [-1] if a negative cycle is reachable from src, else distances
                 (unreachable vertices marked as 10^8).
        """
        INF = 10**18
        dist = [INF] * V                # O(V)
        dist[src] = 0

        # V-1 full relaxation passes  ---- O(V * E)
        for _ in range(V - 1):
            changed = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed = True
            if not changed:             # early exit if no updates in a pass
                break

        # Negative cycle check: one more pass  ---- O(E)
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                return [-1]             # negative cycle reachable from src

        # Map unreachable to 1e8 as requested  ---- O(V)
        UNREACHABLE = 10**8
        return [UNREACHABLE if d == INF else d for d in dist]