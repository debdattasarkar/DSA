#User function Template for python3
class Solution:
	def maxSumIS(self, arr):
		n = len(arr)
        if n == 0:
            return 0

        # dp[i] = max sum of an increasing subsequence that ends at i (must include arr[i])
        dp = arr[:]  # start with the single-element subsequence at each i

        # O(n^2) time: for each i, scan all j < i
        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    # if we can append arr[i] after arr[j], try to improve dp[i]
                    dp[i] = max(dp[i], dp[j] + arr[i])

        # overall max is the answer
        return max(dp)