#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def areElementsContiguous (self, arr): 
        #Complete the function
        unique = set(arr)  # Remove duplicates
        min_val = min(unique)
        max_val = max(unique)

        # Check if every value from min to max is present
        for num in range(min_val, max_val + 1):
            if num not in unique:
                return False  # If any value is missing, not contiguous
        return True  # All numbers are present, so contiguous


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.areElementsContiguous(arr)
        if res:
            print("Yes")
        else :
            print("No")
        # print(res)
        print("~")
        t -= 1


# } Driver Code Ends