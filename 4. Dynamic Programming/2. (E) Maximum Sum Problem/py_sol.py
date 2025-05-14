#User function Template for python3

class Solution:
    def __init__(self):
        self.dp = {}
        
    def maxSum(self, n): 
        # code here 
        # Base case: if n is 0, we return 0
        if n == 0:
            return 0
        if n in self.dp:
            return self.dp[n]
        
        # Recursively break the number
        breakdown = self.maxSum(n//2) + self.maxSum(n//3) + self.maxSum(n//4)
        
        # Store and return the maximum between n and its breakdown
        self.dp[n] = max(n, breakdown)
        return self.dp[n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
        print("~")
# } Driver Code Ends