import heapq
MOD = 10**9 + 7
class Solution:
    def countPaths(self, V, edges):
        """
        Count number of shortest paths from node 0 to node V-1 in
        an undirected weighted graph using Dijkstra.

        dist[v]  = shortest distance from 0 to v
        ways[v]  = number of shortest paths achieving dist[v]

        Time  : O((V + E) log V)   using adjacency list + min heap
        Space : O(V + E)           for graph, dist, ways, heap
        """
        # ---- Build adjacency list ----
        graph = [[] for _ in range(V)]
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))   # undirected

        # ---- Initialize dist and ways ----
        INF = 10**18
        dist = [INF] * V
        ways = [0] * V

        dist[0] = 0          # distance to source is 0
        ways[0] = 1          # exactly 1 way to be at node 0
        # heap items: (current_distance_from_source, node)
        min_heap = [(0, 0)]

        # ---- Dijkstra's algorithm with path counting ----
        while min_heap:
            d_u, u = heapq.heappop(min_heap)

            # If this popped distance is stale, skip
            if d_u > dist[u]:
                continue

            for v, w in graph[u]:
                new_dist = d_u + w

                # Case 1: found a strictly better path to v
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]          # all shortest paths to v pass via u right now
                    heapq.heappush(min_heap, (new_dist, v))

                # Case 2: found another shortest path to v with equal distance
                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        # ways[V-1] is the number of shortest-time paths from 0 to V-1
        return ways[V - 1] % MOD