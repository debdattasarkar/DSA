class Solution:
    def spanningTree(self, V, edges):
        """
        Kruskal's Algorithm with Disjoint Set Union (Union-Find).

        Input:
          V     : number of vertices (0..V-1)
          edges : list of [u, v, w] for undirected graph

        Returns:
          Sum of weights of the MST.

        Complexity:
          - Sort edges: O(E log E)
          - DSU ops:   near O(E α(V)) ~ O(E)
          - Total:     O(E log E)
          - Space:     O(V) for DSU
        """

        # --- Disjoint Set Union (Union-Find) with path compression + union by size ---
        parent = list(range(V))
        size   = [1] * V

        def find(x):
            # Amortized ~O(1) with path compression
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            # Union by size; returns True if merged (i.e., they were in different sets)
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra]  += size[rb]
            return True

        # Sort all edges by weight  -> O(E log E)
        edges.sort(key=lambda e: e[2])

        mst_wt = 0
        picked = 0

        # Greedily pick smallest non-cycle edges
        for u, v, w in edges:
            if union(u, v):             # if this does not create a cycle
                mst_wt += w
                picked += 1
                if picked == V - 1:     # MST complete
                    break

        return mst_wt