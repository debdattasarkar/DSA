#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def removeDuplicates(self, arr):
        # code here 
        seen = set()        # Set to track seen elements
        result = []

        for num in arr:
            if num not in seen:
                result.append(num)   # Keep first occurrence
                seen.add(num)        # Mark as seen
        return result

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicates(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends