#User function Template for python3

class Solution:
    
    # Return a list of lists of integers denoting SCC members.
    # Each SCC sorted; list of SCCs sorted lexicographically.
    def tarjans(self, V, adj):
        disc = [-1] * V         # discovery times
        low  = [0]  * V         # low-link values
        in_stack = [False] * V  # membership in current stack
        st = []                 # active nodes stack
        time = 0
        sccs = []

        def dfs(u):
            nonlocal time
            disc[u] = low[u] = time
            time += 1
            st.append(u); in_stack[u] = True

            for v in adj[u]:
                if disc[v] == -1:
                    # Tree edge
                    dfs(v)
                    low[u] = min(low[u], low[v])
                elif in_stack[v]:
                    # Back edge to an ancestor in the stack
                    low[u] = min(low[u], disc[v])

            # If u is the root of an SCC
            if low[u] == disc[u]:
                comp = []
                while True:
                    w = st.pop()
                    in_stack[w] = False
                    comp.append(w)
                    if w == u:
                        break
                comp.sort()     # sort the individual SCC
                sccs.append(comp)

        for u in range(V):
            if disc[u] == -1:
                dfs(u)

        # Sort the list of SCCs lexicographically
        sccs.sort()
        return sccs