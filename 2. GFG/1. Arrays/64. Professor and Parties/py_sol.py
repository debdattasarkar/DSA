#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def PartyType(self, arr):
        # Your code goes here
        seen = set()
        for color in arr:
            if color in seen:
                return "true"  # duplicate found
            seen.add(color)
        return "false"  # all unique

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        # k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.PartyType(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends