#User function Template for python3

class Solution:
    #Function to return the total number of possible unique BST.
    def numTrees(self,n):
        # dp[k] = number of unique BSTs with k nodes
        dp = [0] * (n + 1)           # O(n) space
        dp[0] = dp[1] = 1            # base cases

        # For each size k, consider all choices of the root i (1..k)
        for k in range(2, n + 1):    # O(n) iterations
            total = 0
            for i in range(1, k + 1):                # O(k) each -> total O(n^2)
                total += dp[i - 1] * dp[k - i]       # combine left & right
            dp[k] = total

        return dp[n]