#User function Template for python3
from collections import deque, defaultdict
class Solution:
    def isPossible(self,N,P,prerequisites):
        """
        Return True if all tasks can be finished (i.e., graph has no cycle).
        Build graph with edges b->a for each pair [a,b].
        Time : O(N + P)
        Space: O(N + P)
        """
        # Build adjacency list and indegree counts
        adj = defaultdict(list)
        indeg = [0] * N
        for a, b in prerequisites:
            adj[b].append(a)   # b must precede a: edge b->a
            indeg[a] += 1

        # Push all nodes with 0 indegree
        q = deque([v for v in range(N) if indeg[v] == 0])

        # Pop and relax edges
        seen = 0
        while q:
            u = q.popleft()
            seen += 1
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # If we processed all nodes, no cycle
        return seen == N