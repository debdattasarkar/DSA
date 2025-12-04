from typing import List
class Solution:
    def minCost(self, costs : List[List[int]]) -> int:
        """
        Optimized DP for "Walls Coloring II"

        Let n = number of walls, k = number of colors.

        dp[i][c] = minimal total cost to paint walls 0..i, with wall i painted color c,
                   and no two adjacent walls sharing the same color.

        Naive transition:
            dp[i][c] = costs[i][c] + min(dp[i-1][p] for p != c)
        is O(k) per (i, c) => O(n * k^2) total.

        Optimization:
            For each row i-1, track:
                - min1_val: smallest dp[i-1][*]
                - min1_color: color index that gives min1_val
                - min2_val: second smallest dp[i-1][*]
            Then:
                if c != min1_color:
                    dp[i][c] = costs[i][c] + min1_val
                else:
                    dp[i][c] = costs[i][c] + min2_val

            So we do O(k) work per row:
                - One pass to compute min1 and min2.
                - One pass to fill row i.
            Total complexity: O(n * k).

        Edge cases:
            - If n == 0: return 0.
            - If k == 0 and n > 0: impossible -> -1.
            - If k == 1 and n > 1: impossible (adjacent walls must differ) -> -1.

        Time  : O(n * k)
        Space : O(k) using rolling array for previous row.
        """
        n = len(costs)
        if n == 0:
            return 0

        # Number of colors
        k = len(costs[0]) if costs[0] else 0

        # Impossible configurations
        if k == 0 and n > 0:
            return -1
        if k == 1:
            # Possible only if at most one wall
            if n == 1:
                return costs[0][0]
            else:
                return -1

        # prev_dp[c] = dp value for previous wall (i-1) with color c
        prev_dp = [0] * k

        # Initialize for first wall: cost equals painting cost
        for c in range(k):
            prev_dp[c] = costs[0][c]

        # Process walls 1..n-1
        for i in range(1, n):
            # -------- Find smallest and second smallest from prev_dp --------
            min1_val = float("inf")
            min2_val = float("inf")
            min1_color = -1

            # One pass O(k)
            for c in range(k):
                val = prev_dp[c]
                if val < min1_val:
                    # current best becomes second best
                    min2_val = min1_val
                    min1_val = val
                    min1_color = c
                elif val < min2_val:
                    min2_val = val

            # -------- Compute new dp row for wall i --------
            curr_dp = [0] * k
            for c in range(k):
                # If we choose same color as previous row's global min,
                # we must use second min to satisfy adjacency constraint.
                if c == min1_color:
                    curr_dp[c] = costs[i][c] + min2_val
                else:
                    curr_dp[c] = costs[i][c] + min1_val

            # Move current row into prev_dp for next iteration
            prev_dp = curr_dp

        # Final answer: minimum cost among all colors for last wall
        return min(prev_dp)