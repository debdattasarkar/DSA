#User function Template for python3

class Solution:
    def transitiveClosure(self, N, graph):
        """
        Warshall's algorithm (boolean Floyd–Warshall).
        reach[i][j] |= reach[i][k] & reach[k][j] for all i,j, for k=0..N-1

        Time  : O(N^3)
        Space : O(N^2) (we store/return the closure)
        """
        # Copy to avoid mutating the caller's matrix (if needed)
        reach = [row[:] for row in graph]

        # Ensure self reachability (path of length 0)
        for i in range(N):
            reach[i][i] = 1

        # k must be the OUTERMOST loop
        for k in range(N):
            for i in range(N):
                if reach[i][k]:                # small prune (common trick)
                    rik = 1
                    row_k = reach[k]
                    row_i = reach[i]
                    for j in range(N):
                        # bottom line: reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
                        if row_k[j]:
                            row_i[j] = 1
        return reach