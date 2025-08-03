#User function Template for python3
class Solution:
	def reverseSubArray(self,arr,l,r):
		# code here
		# Convert 1-based to 0-based indexing
        l -= 1
        r -= 1
    
        # Reverse in-place using two pointers
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        l = int(input())
        r = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.reverseSubArray(arr, l, r)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends