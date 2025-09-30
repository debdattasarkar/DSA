class Solution:
    def maxProfit(self, prices, k):
        # code here
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # Optimization for large k
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))

        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            max_diff = -prices[0]
            for d in range(1, n):
                dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)
                max_diff = max(max_diff, dp[t - 1][d] - prices[d])

        return dp[k][n - 1]

#{ 
 # Driver Code Starts
from collections import deque

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        print(obj.maxProfit(arr, k))
        print("~")
# } Driver Code Ends