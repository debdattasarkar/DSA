class Solution:
	def maximumMatch(self, G):
		"""
        Kuhn's algorithm (DFS-based augmenting paths).
        M = number of applicants (rows), N = number of jobs (cols)

        Time  : O(V * E)  ~ O(M * M * N) worst-case for dense; fits M,N<=100
        Space : O(N) for matchR + O(N) for visited per DFS
        """
        if not G:
            return 0

        M = len(G)
        N = len(G[0]) if G[0] else 0

        # matchR[v] = the applicant currently matched to job v, or -1 if free
        matchR = [-1] * N

        # Try to assign applicant u by DFS-ing for an augmenting path
        def dfs(u, seen):
            for v in range(N):
                # applicant u is interested in job v and v not visited in this DFS
                if G[u][v] and not seen[v]:
                    seen[v] = True
                    # If job v is free, or we can re-assign the current owner to another job
                    if matchR[v] == -1 or dfs(matchR[v], seen):
                        matchR[v] = u
                        return True
            return False

        result = 0
        for u in range(M):
            seen = [False] * N       # reset per DFS (per applicant)
            if dfs(u, seen):
                result += 1
        return result