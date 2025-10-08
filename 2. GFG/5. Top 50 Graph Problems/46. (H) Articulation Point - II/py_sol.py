class Solution:
    def articulationPoints(self, V, edges):
        """
        Tarjan's DFS to find articulation points in an undirected (possibly disconnected) graph.
        Time:  O(V + E)
        Space: O(V + E)
        """

        # Build adjacency list (undirected). Ignore self-loops.
        adj = [[] for _ in range(V)]
        for u, v in edges:
            if u == v:  # self loop doesn't affect articulation logic
                continue
            adj[u].append(v)
            adj[v].append(u)

        disc = [-1] * V             # discovery times
        low = [0] * V               # low-link values
        is_ap = [False] * V         # articulation point flags
        time = 0                    # global DFS timestamp

        def dfs(u: int, parent: int) -> None:
            nonlocal time
            disc[u] = low[u] = time
            time += 1

            child_count = 0  # number of DFS tree children (for root rule)

            for w in adj[u]:
                if w == parent:
                    continue
                if disc[w] == -1:
                    child_count += 1
                    dfs(w, u)

                    # On return, propagate low-link value up
                    low[u] = min(low[u], low[w])

                    # Non-root articulation condition:
                    # If the earliest reachable time from w's subtree is
                    # not earlier than u's discovery, cutting u disconnects that subtree.
                    if parent != -1 and low[w] >= disc[u]:
                        is_ap[u] = True
                else:
                    # Back edge to an ancestor (or already visited neighbor): update low[u]
                    low[u] = min(low[u], disc[w])

            # Root articulation condition:
            if parent == -1 and child_count >= 2:
                is_ap[u] = True

        # Graph can be disconnected: run DFS from every unvisited node.
        for i in range(V):
            if disc[i] == -1:
                dfs(i, -1)

        ans = [i for i, flag in enumerate(is_ap) if flag]
        return ans if ans else [-1]