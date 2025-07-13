
class Solution:
    def nonLisMaxSum(self, arr):
        # code here
        n = len(arr)

        # dp[i][0] = minimum sum of LIS ending at i
        # dp[i][1] = length of LIS ending at i
        dp = [[0, 0] for _ in range(n)]
    
        for i in range(n):
            # Initialize base sum and base length
            dp[i][0] = arr[i]
            dp[i][1] = 1
    
            for j in range(i):
                if arr[i] > arr[j]:
                    # same length LIS can be formed
                    # choose the one with smaller sum
                    if dp[j][1] + 1 == dp[i][1]:
                        dp[i][0] = min(dp[i][0], dp[j][0] + arr[i])
                    # longer LIS can be formed
                    # update both length and sum
                    elif dp[j][1] + 1 > dp[i][1]:
                        dp[i][0] = dp[j][0] + arr[i]
                        dp[i][1] = dp[j][1] + 1
    
        # find maximum LIS length
        maxLen = max(dp[i][1] for i in range(n))
    
        # find minimum sum among LIS of maximum length
        minSum = float('inf')
        for i in range(n):
            if dp[i][1] == maxLen:
                minSum = min(minSum, dp[i][0])
    
        total = sum(arr)
    
        return total - minSum