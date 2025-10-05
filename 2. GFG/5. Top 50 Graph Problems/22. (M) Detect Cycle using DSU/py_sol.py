class Solution:
    # --- find with path compression (amortized ~ O(1)) ---
    def _find(self, x, parent):
        if parent[x] != x:
            parent[x] = self._find(parent[x], parent)  # compress path
        return parent[x]

    # --- union by rank (attach smaller rank under larger) ---
    def _union(self, a, b, parent, rank):
        ra, rb = self._find(a, parent), self._find(b, parent)
        if ra == rb:
            return False  # already in same set -> would form a cycle if used
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[rb] < rank[ra]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1
        return True

    # Function to detect cycle using DSU in an undirected graph.
    def detectCycle(self, V, adj):
        """
        V : number of vertices (0..V-1)
        adj : adjacency list (undirected), i.e., for each edge (u,v), v in adj[u] and u in adj[v]

        Algorithm:
          - Initialize DSU.
          - For each unique edge (u,v) with u < v:
              * If find(u) == find(v) -> cycle -> return 1
              * Else union(u,v)
          - No cycle encountered -> return 0

        Complexity:
          Time  : O(V + E * α(V))  ~ O(V + E)
          Space : O(V)
        """
        parent = [i for i in range(V)]   # O(V)
        rank   = [1] * V                 # O(V)

        # Process each undirected edge exactly once to avoid duplicates.
        for u in range(V):
            for v in adj[u]:
                if u < v:  # ensures (u,v) handled once
                    ru, rv = self._find(u, parent), self._find(v, parent)
                    if ru == rv:
                        return 1        # cycle found
                    # merge components
                    self._union(ru, rv, parent, rank)

        return 0  # no cycle