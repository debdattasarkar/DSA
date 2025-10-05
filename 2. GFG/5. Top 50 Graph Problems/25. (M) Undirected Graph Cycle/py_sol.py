class Solution:
	def isCycle(self, V, edges):
		"""
        Detect cycle in an undirected graph using DSU (Union-Find).
        If an edge connects two vertices already in the same set, a cycle exists.

        Time  : O((V + E) * α(V)) ~ O(V + E)   [α is inverse Ackermann]
        Space : O(V)
        """
        # parent and rank arrays
        parent = list(range(V))  # O(V)
        rank   = [0] * V         # O(V)

        def find(x):
            # Path compression: amortized ~O(1)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            # Union by rank: amortized ~O(1)
            ra, rb = find(a), find(b)
            if ra == rb:
                return False  # already in same set -> using this edge forms a cycle
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
            return True

        for u, v in edges:         # O(E)
            if not union(u, v):    # found cycle
                return True
        return False                # no cycle