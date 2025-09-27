#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3


class Solution:
    def sumExceptFirstLast(self,arr):
        # Parr:  list of pair
        #code here
        # If there are only two elements, return 0
        if len(arr) <= 2:
            return 0
        # Sum from index 1 to len(arr) - 2 (excluding first and last)
        return sum(arr[1:-1])


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.sumExceptFirstLast(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends