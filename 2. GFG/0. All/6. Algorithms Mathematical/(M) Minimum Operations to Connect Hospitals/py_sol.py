class Solution:
    def minConnect(self, V, edges):
        """
        Minimum operations to connect all hospitals into a single component,
        given that we can remove any existing edge and reconnect it elsewhere.

        Approach (Union-Find / Disjoint Set):
        -------------------------------------
        - Treat each hospital as a node in an undirected graph.
        - As we add edges:
            * If edge connects two DIFFERENT components => we UNION them.
            * If edge connects two nodes in the SAME component => it's REDUNDANT.
        - After processing all edges:
            components = number of DSU roots
            redundant = count of redundant edges
        - To connect `components` components, we need `components - 1` edges.
        - If `redundant >= components - 1`:
              return components - 1
          else:
              return -1

        Time Complexity:
            - DSU 'find'/'union' with path compression + union-by-size:
              ~ O(α(V)) per operation (α = inverse Ackermann, almost constant).
            - We process E edges => O((V + E) * α(V)) ≈ O(V + E).
        Space Complexity:
            - parent + size arrays: O(V).
        """

        # ---------- Disjoint Set / Union-Find implementation ----------
        parent = list(range(V))
        size = [1] * V     # or rank, both fine

        def find(x: int) -> int:
            """
            Find with path compression.
            Amortized time ~ O(α(V)).
            """
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> bool:
            """
            Union by size.
            Returns True if a merge happened (distinct components),
            False if x and y were already in the same component.
            """
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False  # no merge; edge is redundant

            # Attach smaller tree under larger
            if size[root_x] < size[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            size[root_x] += size[root_y]
            return True

        # Initially each node is its own component
        components = V
        redundant = 0

        # Process all edges
        # Time: O(E * α(V)) ~ O(E)
        for u, v in edges:
            if union(u, v):
                # merged two components → one less component now
                components -= 1
            else:
                # Did not merge → edge is inside same component => redundant
                redundant += 1

        # Need (components - 1) edges to connect all components
        required = components - 1

        # If we have enough redundant edges, we can rewire them
        if redundant >= required:
            return required
        else:
            return -1