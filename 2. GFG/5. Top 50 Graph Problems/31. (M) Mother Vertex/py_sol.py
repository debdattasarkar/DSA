class Solution:
    # Function to find a Mother Vertex in the Graph (Optimal: O(V + E)).
    # Steps:
    # 1) One DFS sweep to get a 'candidate' (last finished vertex).
    # 2) Verify candidate reaches all vertices.
    # 3) Return the minimum index inside candidate's SCC (Kosaraju 2nd pass from top of stack on transpose).
    #Function to find a Mother Vertex in the Graph.
	def findMotherVertex(self, V, adj):
		# ----- 1) finishing-time DFS to get candidate -----
        visited = [False] * V
        order = []  # We’ll push vertices after exploring all descendants (postorder)
        
        def dfs1(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs1(v)
            order.append(u)
        
        for u in range(V):
            if not visited[u]:
                dfs1(u)
        
        candidate = order[-1]  # last finished vertex
        
        # ----- 2) verify candidate reaches everyone -----
        def count_reach(start):
            seen = [False] * V
            stack = [start]
            seen[start] = True
            cnt = 1
            while stack:
                x = stack.pop()
                for y in adj[x]:
                    if not seen[y]:
                        seen[y] = True
                        cnt += 1
                        stack.append(y)
            return cnt
        
        if count_reach(candidate) != V:
            return -1  # No mother vertex exists
        
        # ----- 3) return MIN index among candidate's SCC -----
        # Build transpose graph (reverse edges): O(V + E)
        tr = [[] for _ in range(V)]
        for u in range(V):
            for v in adj[u]:
                tr[v].append(u)
        
        # Kosaraju: on transpose, a DFS from candidate (as top of stack) yields its SCC.
        comp = []
        seen2 = [False] * V
        stack = [candidate]
        seen2[candidate] = True
        while stack:
            u = stack.pop()
            comp.append(u)
            for w in tr[u]:
                if not seen2[w]:
                    seen2[w] = True
                    stack.append(w)
        
        # Any vertex inside the source SCC is a mother; we return the MIN index per problem.
        return min(comp)