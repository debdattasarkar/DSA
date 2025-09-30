class Solution:
    def maxProfit(self, prices, k):
        """
        Optimized DP: O(n*k) time, O(k) extra space.
        Early exit: if k >= n//2, do unlimited-transactions greedy in O(n).
        """
        n = len(prices)
        if n <= 1 or k == 0:
            return 0

        # Unlimited transactions case -> sum of positive deltas (O(n) time, O(1) space)
        if k >= n // 2:
            prof = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    prof += prices[i] - prices[i-1]
            return prof

        # DP over transactions: arrays of length k+1 (1..k used)
        import math
        buy  = [-math.inf] * (k + 1)  # buy[t]  = best cash after buy of t-th transaction
        sell = [0] * (k + 1)          # sell[t] = best cash after sell of t-th transaction

        # Iterate each price once (O(n)); inner loop over t=1..k (O(k)) -> O(n*k)
        for p in prices:
            # Go forward t=1..k (no need to go backward because we read sell[t-1] from previous t)
            for t in range(1, k + 1):
                buy[t]  = max(buy[t],  sell[t-1] - p)  # start/extend holding for t-th txn
                sell[t] = max(sell[t], buy[t] + p)     # finish t-th txn

        return sell[k]