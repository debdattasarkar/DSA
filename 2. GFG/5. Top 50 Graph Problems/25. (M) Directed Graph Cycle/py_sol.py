
class Solution:
    def isCycle(self, V, edges):
        """
        Detect a cycle in a directed graph using DFS + recursion stack.
        Steps:
          1) Build adjacency list: O(V+E)
          2) DFS each unvisited node keeping a recursion-stack flag.
             If we reach a node that is on the current recursion stack,
             we found a back edge -> cycle.
        Time  : O(V + E)
        Space : O(V + E) for graph + O(V) recursion/visited
        """
        # 1) Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)

        visited = [False] * V     # permanently finished nodes
        in_stack = [False] * V    # nodes on current DFS path

        def dfs(u: int) -> bool:
            visited[u] = True
            in_stack[u] = True
            for w in adj[u]:
                if not visited[w]:
                    if dfs(w):               # cycle detected below
                        return True
                elif in_stack[w]:
                    # Back edge to a node currently in recursion stack -> cycle
                    return True
            in_stack[u] = False              # backtrack
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        return False