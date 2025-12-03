class Solution:
	def tsp(self, cost):
		"""
        DP with bitmask solution to TSP starting and ending at city 0.

        State:
            dp[mask][u] = min cost to start at 0, visit exactly the cities in 'mask',
                          and end at city u.  'mask' is a bitmask of visited cities.

        Transition:
            From (mask, u) go to any unvisited v:
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + cost[u][v])

        Initialization:
            dp[1 << 0][0] = 0   # only city 0 visited, at city 0

        Answer:
            FULL = (1 << n) - 1
            ans  = min over u: dp[FULL][u] + cost[u][0]

        Complexity:
            n cities, M = 2^n masks
            Time  : O(n^2 * M)
            Space : O(n * M)
        """
        n = len(cost)
        if n == 0:
            return 0

        FULL_MASK = (1 << n) - 1
        INF = 10**18

        # dp[mask][u] table
        dp = [[INF] * n for _ in range(1 << n)]

        # Only city 0 visited, at city 0
        dp[1][0] = 0   # mask 000...001

        # Iterate over all masks
        for mask in range(1 << n):
            # We must always include city 0 (bit 0) in the path
            if not (mask & 1):
                continue

            for u in range(n):
                if dp[mask][u] == INF:
                    # This state hasn't been reached
                    continue

                # Try to go to each city v that is not yet visited in 'mask'
                for v in range(n):
                    if mask & (1 << v):   # bit v already set => city v visited
                        continue

                    new_mask = mask | (1 << v)
                    new_cost = dp[mask][u] + cost[u][v]

                    if new_cost < dp[new_mask][v]:
                        dp[new_mask][v] = new_cost

        # Close tour: all cities visited, return to 0
        answer = INF
        for u in range(n):   # include u=0 so n=1 works
            if dp[FULL_MASK][u] == INF:
                continue
            total_cost = dp[FULL_MASK][u] + cost[u][0]
            if total_cost < answer:
                answer = total_cost

        # Safety fallback (should not happen for valid TSP)
        if answer == INF:
            return 0
        return answer