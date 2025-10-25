class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, arr):
        n = len(arr)
        i = 0
        total_profit = 0

        while i < n - 1:
            # 1) Find next valley (strictly lower than next or equal handled)
            while i < n - 1 and arr[i + 1] <= arr[i]:
                i += 1
            if i == n - 1:  # no valley => no more profit
                break
            buy_price = arr[i]
            i += 1

            # 2) Climb to the next peak (non-decreasing)
            while i < n and arr[i] >= arr[i - 1]:
                i += 1
            sell_price = arr[i - 1]

            total_profit += sell_price - buy_price

        return total_profit