from collections import defaultdict, deque

class Solution:
    def findOrder(words):
        """
        Return one valid alien letter order or "" if impossible.

        Steps:
          1) Gather all unique letters.
          2) Build graph from adjacent word pairs using the first differing char.
             - If w1 is a strict prefix of w2 => OK
             - If w2 is a strict prefix of w1 (no diff, len(w1) > len(w2)) => invalid -> ""
          3) Kahn's BFS topological sort over letters (nodes).
          4) If we placed all letters, return the order. Else, there's a cycle -> "".

        Time:  O(n * m + V + E)  ; n=#words, m=avg length, V<=26, E<=25*? (small)
        Space: O(V + E)
        """
        if not words:
            return ""

        # 1) Unique letters
        letters = set(ch for w in words for ch in w)

        # 2) Build graph
        adj = defaultdict(set)           # u -> set of v
        indeg = {ch: 0 for ch in letters}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # prefix check if needed
            minlen = min(len(w1), len(w2))
            j = 0
            while j < minlen and w1[j] == w2[j]:
                j += 1
            if j == minlen:
                # No differing char in overlap; if w1 longer than w2 => invalid
                if len(w1) > len(w2):
                    return ""
                continue
            # First differing chars create an edge w1[j] -> w2[j]
            u, v = w1[j], w2[j]
            if v not in adj[u]:          # avoid double-indegree
                adj[u].add(v)
                indeg[v] += 1

        # 3) Kahn's BFS
        q = deque([c for c in indeg if indeg[c] == 0])
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # 4) Cycle check
        if len(order) != len(letters):
            return ""  # cycle or unreachable nodes
        return "".join(order)