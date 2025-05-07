#User function Template for python3

class Solution:
    
    def KthMissingElement(self,arr,k) : 
        #Complete the function
        n = len(arr)

        for i in range(1, n):
            # Calculate how many numbers are missing between arr[i-1] and arr[i]
            missing = arr[i] - arr[i - 1] - 1

            if k <= missing:
                # If k is within the missing range, return the result
                return arr[i - 1] + k

            # Otherwise, skip these missing numbers
            k -= missing

        # If k-th missing is beyond the last element
        return -1


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
        res = ob.KthMissingElement(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends