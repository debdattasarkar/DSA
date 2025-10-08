class Solution:
    def isBipartite(self, V, edges):
        # Build adjacency list; O(V + E)
        adj = [[] for _ in range(V)]
        for u, v in edges:
            if u == v:               # self-loop => cannot be bipartite
                return False
            adj[u].append(v)
            adj[v].append(u)
        
        color = [-1] * V             # -1 = uncolored; 0/1 are the two colors
        
        for s in range(V):           # cover disconnected graphs
            if color[s] != -1:
                continue
            # BFS from s
            color[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for w in adj[u]:
                    if color[w] == -1:
                        color[w] = color[u] ^ 1  # opposite color
                        q.append(w)
                    elif color[w] == color[u]:
                        return False             # conflict
        return True                               # all components colored without conflicts