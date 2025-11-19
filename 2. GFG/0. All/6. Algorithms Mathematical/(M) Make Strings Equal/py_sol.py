class Solution:
    def minCost(self, s, t, transform, cost):
        """
        Make strings s and t equal with minimum total transformation cost.

        Approach:
        ---------
        1) Model 26 letters as nodes in a directed weighted graph.
           Edge (x -> y) with weight w means we can transform x into y with cost w.
        2) Run Floyd–Warshall to compute all-pairs shortest paths on this 26-node graph.
           dist[u][v] = minimal cost to transform char u into char v.
        3) For each index i, compute:
               best_cost_i = min over c ( dist[s[i]][c] + dist[t[i]][c] )
           Sum all best_cost_i. If for some i all paths are impossible,
           return -1.

        Time Complexity:
            - Building dist:     O(#transforms)  ≤ 500
            - Floyd–Warshall:   O(26^3) ≈ constant
            - Per-character sum: O(n * 26)
            => Overall: O(n * 26) ~ O(n)
        Space Complexity:
            - dist matrix: O(26^2) (constant)
        """

        n = len(s)
        if n != len(t):
            # Problem states they are equal, but we guard anyway
            return -1

        ALPHABET = 26
        INF = 10**18  # large enough

        # Helper to map 'a'..'z' -> 0..25
        def idx(ch: str) -> int:
            return ord(ch) - ord('a')

        # 1) Initialize distance matrix
        #    dist[u][v] = minimal cost to go u -> v
        dist = [[INF] * ALPHABET for _ in range(ALPHABET)]

        # Zero cost from a letter to itself
        for u in range(ALPHABET):
            dist[u][u] = 0

        # Add direct transformation edges
        # Multiple edges between same pair: keep the cheapest.
        for (x, y), w in zip(transform, cost):
            u = idx(x)
            v = idx(y)
            if w < dist[u][v]:
                dist[u][v] = w

        # 2) Floyd–Warshall: try all intermediate letters k
        #    For each triple (i, j, k):
        #        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        #
        #    Time: O(26^3) ~ constant
        for k in range(ALPHABET):
            dk = dist[k]   # small micro-optimization (row reference)
            for i in range(ALPHABET):
                dik = dist[i][k]
                if dik == INF:
                    continue
                di = dist[i]
                # Relax edges i -> j via k
                for j in range(ALPHABET):
                    via_k = dik + dk[j]
                    if via_k < di[j]:
                        di[j] = via_k

        # 3) For each position i in strings:
        #       if s[i] == t[i], cost_i = 0 (already equal)
        #       else:
        #           best_i = min_c dist[s[i]][c] + dist[t[i]][c]
        #           if best_i == INF, impossible -> return -1
        total_cost = 0

        for i in range(n):
            ch_s = s[i]
            ch_t = t[i]

            if ch_s == ch_t:
                # No cost needed; we can just keep both as they are.
                continue

            u = idx(ch_s)
            v = idx(ch_t)

            best_here = INF

            # Try all possible target letters c (0..25)
            for c in range(ALPHABET):
                cost_s_to_c = dist[u][c]
                cost_t_to_c = dist[v][c]
                if cost_s_to_c == INF or cost_t_to_c == INF:
                    # At least one is impossible -> skip this c
                    continue
                candidate = cost_s_to_c + cost_t_to_c
                if candidate < best_here:
                    best_here = candidate

            if best_here == INF:
                # There is no common letter we can transform both into.
                return -1

            total_cost += best_here

        return total_cost