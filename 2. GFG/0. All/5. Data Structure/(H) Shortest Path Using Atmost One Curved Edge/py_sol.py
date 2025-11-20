import heapq
from typing import List
class Solution:
    def shortestPath(self, V, a, b, edges):
        """
        Compute the shortest path from a to b using at most one curved edge.

        V      : number of vertices (0..V-1)
        a, b   : source and destination vertices
        edges  : list of [x, y, w1, w2]
                 - w1 = weight of straight edge x<->y
                 - w2 = weight of curved edge  x<->y

        Approach:
        ---------
        1) Build adjacency for STRAIGHT edges only (using w1).
        2) Run Dijkstra from 'a' on straight graph -> dist_from_a.
        3) Run Dijkstra from 'b' on straight graph -> dist_from_b.
        4) Candidate 0-curved: dist_from_a[b].
        5) For each edge (x,y,w1,w2), evaluate using its curved edge once:
               cand1 = dist_from_a[x] + w2 + dist_from_b[y]
               cand2 = dist_from_a[y] + w2 + dist_from_b[x]
           Take minimum over all such candidates.
        6) Answer = min(0-curved candidate, best curved candidate).
           If answer is INF, return -1.

        Time Complexity:
            - Building adjacency: O(E)
            - Each Dijkstra:      O((V + E) log V)
            - Edge scan:          O(E)
            => Overall:           O((V + E) log V)

        Space Complexity:
            - Adjacency + distance arrays: O(V + E)
        """

        # ---------------- helper: Dijkstra on straight-edge graph -----------
        def dijkstra(start: int, adj: List[List[tuple]]) -> List[int]:
            INF = 10**18
            dist = [INF] * V
            dist[start] = 0
            min_heap = [(0, start)]          # (distance, vertex)

            while min_heap:
                current_dist, u = heapq.heappop(min_heap)
                if current_dist > dist[u]:
                    continue  # outdated entry

                for v, weight in adj[u]:
                    new_dist = current_dist + weight
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(min_heap, (new_dist, v))

            return dist

        # Build adjacency list for straight edges (w1)
        # Time: O(E), Space: O(V + E)
        adj_straight = [[] for _ in range(V)]
        for x, y, w1, w2 in edges:
            adj_straight[x].append((y, w1))
            adj_straight[y].append((x, w1))

        INF = 10**18

        # Dijkstra from a and from b on straight edges only
        dist_from_a = dijkstra(a, adj_straight)
        dist_from_b = dijkstra(b, adj_straight)

        # Candidate using NO curved edges
        answer = dist_from_a[b]

        # Consider paths using exactly ONE curved edge
        # Time: O(E)
        best_with_curved = INF
        for x, y, w1, w2 in edges:
            # if either end is unreachable via straight edges, skip
            if dist_from_a[x] != INF and dist_from_b[y] != INF:
                cand1 = dist_from_a[x] + w2 + dist_from_b[y]
                if cand1 < best_with_curved:
                    best_with_curved = cand1
            if dist_from_a[y] != INF and dist_from_b[x] != INF:
                cand2 = dist_from_a[y] + w2 + dist_from_b[x]
                if cand2 < best_with_curved:
                    best_with_curved = cand2

        answer = min(answer, best_with_curved)

        return -1 if answer >= INF else answer