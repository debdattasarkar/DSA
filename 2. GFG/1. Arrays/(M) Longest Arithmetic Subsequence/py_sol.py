#User function Template for python3
from collections import defaultdict

class Solution:
    def lengthOfLongestAP(self,arr):
        # code here
        n = len(arr)
        if n <= 2:
            return n

        dp = [defaultdict(int) for _ in range(n)]
        max_len = 2

        for i in range(n):
            for j in range(i):
                diff = arr[i] - arr[j]
                # Extend the AP ending at j with the same diff
                dp[i][diff] = dp[j][diff] + 1 if diff in dp[j] else 2
                max_len = max(max_len, dp[i][diff])

        return max_len