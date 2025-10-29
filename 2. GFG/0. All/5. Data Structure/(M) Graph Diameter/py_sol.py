from collections import deque, defaultdict

class Solution:
    def diameter(self, V, edges):
        """
        Two-BFS/DFS trick (handles forest by taking max per component).
        Time  : O(V + E)     -- each edge visited O(1) per BFS
        Space : O(V)         -- adjacency + queues/visited
        """
        if V == 0:
            return 0

        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(src):
            """Return (farthest_node, farthest_dist) from src."""
            dist = [-1] * V
            q = deque([src])
            dist[src] = 0
            far_node, far_dist = src, 0
            while q:
                x = q.popleft()
                for nbr in graph[x]:
                    if dist[nbr] == -1:
                        dist[nbr] = dist[x] + 1
                        q.append(nbr)
                        if dist[nbr] > far_dist:
                            far_dist = dist[nbr]
                            far_node = nbr
            return far_node, far_dist

        visited = [False] * V
        answer = 0

        # In case the graph is a forest, compute diameter per component
        for s in range(V):
            if visited[s]:
                continue
            # 1) Discover this component (O(size_of_component))
            comp = []
            q = deque([s])
            visited[s] = True
            while q:
                x = q.popleft()
                comp.append(x)
                for y in graph[x]:
                    if not visited[y]:
                        visited[y] = True
                        q.append(y)

            # 2) Two BFS within this component
            a, _ = bfs(comp[0])   # farthest from an arbitrary node
            _, d = bfs(a)         # farthest from 'a' → component diameter
            answer = max(answer, d)

        return answer
