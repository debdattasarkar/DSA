class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, arr):
        """
        Sum-of-positives greedy:
        Add price[i+1] - price[i] whenever it's positive.
        Time:  O(n)  (single pass)
        Space: O(1)  (constant extra)
        """
        profit = 0
        for i in range(len(arr) - 1):
            if arr[i + 1] > arr[i]:
                profit += arr[i + 1] - arr[i]
        return profit