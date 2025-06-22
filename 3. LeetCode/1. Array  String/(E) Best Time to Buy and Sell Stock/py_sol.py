class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Found a better day to buy
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)  # Better profit found

        return max_profit
