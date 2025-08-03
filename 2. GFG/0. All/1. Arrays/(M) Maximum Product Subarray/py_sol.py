#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
	    # code here
	    if not arr:
            return 0

        max_prod = min_prod = res = arr[0]

        for num in arr[1:]:
            # Handle negative by swapping
            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            # Extend or restart at current number
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            res = max(res, max_prod)

        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends