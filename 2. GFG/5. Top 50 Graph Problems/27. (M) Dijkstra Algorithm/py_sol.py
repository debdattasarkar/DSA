class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # Build adjacency list: O(E)
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # Since the graph is undirected

        # Distance array initialized to infinity
        dist = [float('inf')] * V
        dist[src] = 0

        # Min-heap to get the minimum distance vertex fast
        minHeap = [(0, src)]  # (distance, node)

        while minHeap:
            curr_dist, u = heapq.heappop(minHeap)

            # Traverse all adjacent vertices
            for v, weight in adj[u]:
                if dist[v] > curr_dist + weight:
                    dist[v] = curr_dist + weight
                    heapq.heappush(minHeap, (dist[v], v))

        return dist