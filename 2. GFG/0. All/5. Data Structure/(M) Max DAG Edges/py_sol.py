class Solution:
    def maxEdgesToAdd(self, V, edges):
        """
        Max edges in any DAG on V nodes (for some topological order) = V*(V-1)/2.
        Current edges = E = len(edges).
        Answer = V*(V-1)/2 - E.

        Time  : O(1)
        Space : O(1)
        """
        E = len(edges)
        max_possible = V * (V - 1) // 2
        return max_possible - E