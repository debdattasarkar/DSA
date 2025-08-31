#User function template for Python

class Solution:
	def floydWarshall(self, dist):
		#Code here
		"""
        In-place APSP with intermediate node DP.
        Time:  O(n^3)
        Space: O(1) extra (besides the dist matrix we modify)
        """
        n = len(dist)
        INF = 10**8  # sentinel for "no path"

        # k = intermediate node we are allowed to use
        for k in range(n):                                # O(n)
            dk = dist[k]                                  # local ref (micro-optimization)
            for i in range(n):                            # O(n)
                # If i->k is INF, no path via k for this i
                dik = dist[i][k]
                if dik == INF:
                    continue
                row_i = dist[i]
                for j in range(n):                        # O(n)
                    # Skip if k->j is INF
                    dj = dk[j]
                    if dj == INF:
                        continue
                    # Try to improve i->j via k
                    new_cost = dik + dj
                    if new_cost < row_i[j]:
                        row_i[j] = new_cost
        # dist mutated in place
        return dist