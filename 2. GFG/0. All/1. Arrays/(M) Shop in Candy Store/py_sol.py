class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        """
        Returns [min_cost, max_cost] using the classic greedy with two pointers.
        Time:  O(n log n) due to sorting
        Space: O(1) extra (sorting in place)
        """
        prices.sort()  # sort ascending once

        # ---- Minimum cost: buy cheapest, take k costliest for free ----
        i, j, min_cost = 0, len(prices) - 1, 0
        while i <= j:
            # pay for the cheapest remaining
            min_cost += prices[i]       # O(1)
            i += 1                      # move past the purchased one
            j -= k                      # take up to k freebies from the right

        # ---- Maximum cost: buy costliest, take k cheapest for free ----
        i, j, max_cost = 0, len(prices) - 1, 0
        while i <= j:
            # pay for the costliest remaining
            max_cost += prices[j]       # O(1)
            j -= 1                      # move past the purchased one
            i += k                      # take up to k freebies from the left

        return [min_cost, max_cost]