#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:

	def nextGreatest(self,arr):
		# code  here
		n = len(arr)
        maxRight = -1  # Initially, there's no element to the right
        for i in range(n - 1, -1, -1):  # Traverse from end to start
            current = arr[i]  # Store the current element
            arr[i] = maxRight  # Replace with the greatest on the right
            if current > maxRight:
                maxRight = current  # Update maxRight if current is greater
        return arr


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.nextGreatest(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends