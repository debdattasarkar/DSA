from typing import List
from collections import deque
class Solution:
    def secondMST(self, V, edges):
        # --------- DSU (Union-Find) ----------
        parent = list(range(V))
        size = [1] * V

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> bool:
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]
            return True

        # ---------- 1) Build *one* MST using Kruskal ----------
        # sorted_edges: (w, u, v, original_index)
        sorted_edges = sorted(
            (w, u, v, i) for i, (u, v, w) in enumerate(edges)
        )

        in_mst = [False] * len(edges)
        mst_weight = 0
        edges_used = 0

        for w, u, v, idx in sorted_edges:
            if union(u, v):
                in_mst[idx] = True
                mst_weight += w
                edges_used += 1
                if edges_used == V - 1:
                    break

        # If graph not connected -> no MST, hence no second MST
        if edges_used != V - 1:
            return -1

        # ---------- 2) Build adjacency list for MST ----------
        # Store (neighbor, (edge_index, weight)) so we can identify edges on path.
        mst_adj = [[] for _ in range(V)]
        for idx, (u, v, w) in enumerate(edges):
            if in_mst[idx]:
                mst_adj[u].append((v, (idx, w)))
                mst_adj[v].append((u, (idx, w)))

        # ---------- Helper: get path edges between u and v in MST ----------
        def get_path_edges(u: int, v: int):
            """
            Returns list of (edge_index, weight) along the unique path u->v in MST.
            Uses BFS to reconstruct path. Complexity: O(V).
            """
            visited = [False] * V
            parent_node = [-1] * V        # parent vertex in BFS tree
            parent_edge = [None] * V      # (edge_index, weight) used to reach this node

            queue = deque([u])
            visited[u] = True

            while queue:
                node = queue.popleft()
                if node == v:
                    break
                for nei, (eid, w) in mst_adj[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        parent_node[nei] = node
                        parent_edge[nei] = (eid, w)
                        queue.append(nei)

            if not visited[v]:
                return []  # shouldn't happen in a connected MST

            # Reconstruct path edges by walking back from v to u
            path_edges = []
            cur = v
            while cur != u:
                eid, w = parent_edge[cur]
                path_edges.append((eid, w))
                cur = parent_node[cur]

            return path_edges  # order doesn't matter

        # ---------- 3) Try every non-MST edge and every edge on its cycle ----------
        second_best = float('inf')

        for idx, (u, v, w) in enumerate(edges):
            if in_mst[idx]:
                continue  # skip MST edges

            # Edges on the cycle created by adding (u, v, w)
            path_edges = get_path_edges(u, v)

            for eid, w_on_path in path_edges:
                candidate = mst_weight + w - w_on_path
                # Must be strictly greater than MST weight
                if mst_weight < candidate < second_best:
                    second_best = candidate

        return -1 if second_best == float('inf') else second_best