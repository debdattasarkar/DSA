#User function Template for python3

class Solution:
    def isCircle(self, arr):
        """
        Graph view:
          - Vertices: 26 letters [0..25] for 'a'..'z'
          - Each string s adds a directed edge u->v where u=s[0], v=s[-1]
        Condition for circle of ALL strings = Eulerian cycle over all edges:
          1) In-degree[v] == Out-degree[v] for all vertices
          2) All vertices with nonzero degree lie in one strongly-connected component
             (on the directed graph)

        Time  : O(V + E) = O(26 + n) ~ O(n)
        Space : O(V + E) = O(26 + n) ~ O(n)
        """
        if not arr:
            return 0

        V = 26
        adj = [[] for _ in range(V)]
        rev = [[] for _ in range(V)]
        indeg = [0] * V
        outdeg = [0] * V
        active = [False] * V   # vertex appears in any edge

        def idx(ch): return ord(ch) - 97  # 'a' -> 0

        # Build graph ------------------------------------------------ O(n)
        for s in arr:
            u = idx(s[0])
            v = idx(s[-1])
            adj[u].append(v)
            rev[v].append(u)
            outdeg[u] += 1
            indeg[v] += 1
            active[u] = active[v] = True

        # 1) Balanced degrees ---------------------------------------- O(V)
        for v in range(V):
            if indeg[v] != outdeg[v]:
                return 0

        # Find a start vertex that has edges
        start = -1
        for v in range(V):
            if outdeg[v] > 0:
                start = v
                break
        if start == -1:
            # No edges at all (all strings length>=1 per constraints, but just in case)
            return 0

        # 2) Strong connectivity: DFS on adj and on rev --------------- O(V+E)
        def dfs(graph, s, seen):
            stack = [s]
            seen[s] = True
            while stack:
                u = stack.pop()
                for w in graph[u]:
                    if not seen[w]:
                        seen[w] = True
                        stack.append(w)

        seen1 = [False] * V
        dfs(adj, start, seen1)
        for v in range(V):
            if active[v] and not seen1[v]:
                return 0

        seen2 = [False] * V
        dfs(rev, start, seen2)
        for v in range(V):
            if active[v] and not seen2[v]:
                return 0

        return 1