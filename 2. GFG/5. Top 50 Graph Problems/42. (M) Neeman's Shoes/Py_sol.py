#User function Template for python3
import heapq
class Solution:
    def exercise(self, N, M, A,src, dest,X):
        """
        Return which shoes Geek buys based on the shortest path distance
        between src and dest compared to X.

        Graph: undirected, non-negative weights -> Dijkstra
        Time  : O((N + M) log N) using adjacency list + min-heap
        Space : O(N + M) for adjacency + O(N) for dist/heap
        """
        # 1) Build adjacency list: O(N + M)
        adj = [[] for _ in range(N)]
        for u, v, w in A:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # 2) Dijkstra from src: O((N + M) log N)
        INF = 10**20
        dist = [INF] * N
        dist[src] = 0
        # heap entries: (distance_so_far, node)
        heap = [(0, src)]

        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                # stale entry; skip (heap optimization)
                continue
            if u == dest:
                # early exit: shortest distance to dest is finalized
                break
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        # 3) Decide based on distance
        dmin = dist[dest]
        # If unreachable, dmin stays INF -> definitely > X -> Joggers
        if dmin <= X:
            return "Neeman's Cotton Classics"
        else:
            return "Neeman's Wool Joggers"