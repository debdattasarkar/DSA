class Solution:
    def maxProfit(self, arr):
        """
        3-state DP with O(1) space:
            hold: max profit holding a stock at end of day i
            sold: max profit just sold today
            rest: max profit holding nothing & not selling today
        Time:  O(n)   (single pass)
        Space: O(1)   (three scalars)
        """
        if not arr:
            return 0

        NEG_INF = -10**18
        hold = -arr[0]     # buy on day 0
        sold = NEG_INF     # cannot sell on day 0
        rest = 0           # do nothing day 0

        for price in arr[1:]:
            prev_hold, prev_sold, prev_rest = hold, sold, rest

            # hold: keep holding OR buy today from resting state
            hold = max(prev_hold, prev_rest - price)

            # sold: must have held yesterday, sell today
            sold = prev_hold + price

            # rest: either keep resting or just cooled down after a sell
            rest = max(prev_rest, prev_sold)

        # End profit must be without a stock in hand
        return max(sold, rest)