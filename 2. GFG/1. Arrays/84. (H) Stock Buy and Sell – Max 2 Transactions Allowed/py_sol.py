class Solution:
    def maxProfit(self, prices):
        # code here
        n = len(prices)
        if n == 0:
            return 0

        # Left to right: max profit with 1st transaction ending at i
        left_profit = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left_profit[i] = max(left_profit[i - 1], prices[i] - min_price)

        # Right to left: max profit with 2nd transaction starting at i
        right_profit = [0] * n
        max_price = prices[-1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right_profit[i] = max(right_profit[i + 1], max_price - prices[i])

        # Combine the two profits
        max_total = 0
        for i in range(n):
            max_total = max(max_total, left_profit[i] + right_profit[i])

        return max_total


#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends