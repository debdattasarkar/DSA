from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        """
        Start at node 0, traverse neighbors in the given adjacency order.
        Time:  O(V + E)  -- each node/edge processed a constant number of times
        Space: O(V)      -- visited + queue
        """
        V = len(adj)
        order = []
        if V == 0:
            return order

        visited = [False] * V
        q = deque()

        # BFS root is fixed at 0 per problem statement
        visited[0] = True
        q.append(0)

        while q:
            u = q.popleft()          # O(1)
            order.append(u)
            for v in adj[u]:         # iterate in given order
                if not visited[v]:
                    visited[v] = True
                    q.append(v)      # enqueue once per vertex

        return order
        