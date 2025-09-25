# Your task is to complete this function
# Function should return an integer
class Solution:
    def minSum(self,arr):
        """
        dp[i] = arr[i] + min(dp[i+1], dp[i+2], dp[i+3], dp[i+4])
        Answer = min(dp[0], dp[1], dp[2], dp[3])  (use only existing indices)
        
        Time:  O(n)   (constant 4 lookups per i)
        Space: O(n)   (dp array)
        """
        n = len(arr)
        if n == 0:
            return 0  # not in constraints, but safe
        # Create dp with padding so slices beyond n are zero
        K = 4
        dp = [0] * (n + K)  # dp[n..n+3] = 0 acts as base
        
        # Fill from right to left
        for i in range(n - 1, -1, -1):
            # min over the next 4 dp's (constant-time since K=4)
            dp[i] = arr[i] + min(dp[i + 1], dp[i + 2], dp[i + 3], dp[i + 4])
        
        # The first pick must be within the first 4 indices (or all if n<4)
        upto = min(K, n)
        return min(dp[0:upto])