class Solution:
	def minCoins(self, coins, sum):
		# code here
        dp = [float('inf')] * (sum + 1)
        dp[0] = 0  # 0 coins to make sum 0

        for coin in coins:
            for i in range(coin, sum + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[sum] if dp[sum] != float('inf') else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCoins(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends