
from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        """
        Build adjacency list for an undirected graph.
        - Initialize V empty lists: O(V)
        - For each edge (u,v), append both ways: O(E)
        - Sort every neighbor list for deterministic output: sum O(deg(i) log deg(i))
          which overall is O(E log(max_deg)) in worst case.
        
        Time   : O(V + E + sum log(deg(i)))  ~ O(V + E log E) worst-case dense sort
        Space  : O(V + E) for adjacency storage
        """
        adj = [[] for _ in range(V)]          # O(V)

        for u, v in edges:                    # O(E)
            adj[u].append(v)
            adj[v].append(u)

        for i in range(V):                    # total O(E log deg(i)) over all i
            adj[i].sort()

        return adj