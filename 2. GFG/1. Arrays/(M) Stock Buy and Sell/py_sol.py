#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function template for Python

class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, arr):
        # code here
        profit = 0
        for i in range(1, len(arr)):
            # Add profit from every increasing pair
            if arr[i] > arr[i - 1]:
                profit += arr[i] - arr[i - 1]
        return profit


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.stockBuySell(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends