from collections import deque, defaultdict
class Solution:
    def findOrder(self, n, prerequisites):
        """
        Kahn's Algorithm (BFS on in-degrees) for Topological Sort.
        Time  : O(n + m) where m = len(prerequisites)
        Space : O(n + m) for adjacency + in-degree + queue + output
        """
        # Build graph: y -> x for [x, y]
        adj = defaultdict(list)
        in_degree = [0] * n
        for x, y in prerequisites:
            adj[y].append(x)
            in_degree[x] += 1

        # Start with courses that have no prerequisites
        q = deque([v for v in range(n) if in_degree[v] == 0])
        order = []

        # BFS: always take something available (in_degree == 0)
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)

        # If we scheduled all n courses, return order; else cycle -> impossible
        return order if len(order) == n else []