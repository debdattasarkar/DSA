#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        prefix = {}  # maps balance to earliest index
        Sum = 0      # balance: +1 for >k, -1 for <=k
        maxLen = 0

        for i in range(len(arr)):
            # Update balance
            Sum += 1 if arr[i] > k else -1

            # If more elements > k till now
            if Sum > 0:
                maxLen = i + 1
            else:
                # Check for (Sum - 1) previously seen
                if (Sum - 1) in prefix:
                    maxLen = max(maxLen, i - prefix[Sum - 1])

            # Store the first occurrence of this balance
            if Sum not in prefix:
                prefix[Sum] = i

        return maxLen

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        
        arr = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        print("~")
        t -= 1
# } Driver Code Ends