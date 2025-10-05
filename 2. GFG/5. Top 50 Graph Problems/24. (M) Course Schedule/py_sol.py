class Solution:
    def findOrder(self, n, prerequisites):
        """
        Return any topological order of courses (0..n-1) or [] if impossible.
        Each pair [a, b] means b -> a (b is a prereq for a).

        Time  : O(n + m)  where m = len(prerequisites)
        Space : O(n + m)
        """
        # Build adjacency and indegree
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for a, b in prerequisites:
            adj[b].append(a)   # edge b -> a
            indeg[a] += 1

        # Start with all nodes with indegree 0
        from collections import deque
        q = deque([i for i in range(n) if indeg[i] == 0])

        order = []
        while q:
            u = q.popleft()
            order.append(u)
            # Decrease indegree of neighbors; push new zeros
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # If we processed all nodes, we found an order; otherwise there's a cycle
        return order if len(order) == n else []