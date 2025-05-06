#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        n = len(arr)
        
        # Step 1: Combine adjacent valid equal elements
        i = 0
        while i < n - 1:
            if arr[i] != 0 and arr[i] == arr[i + 1]:
                arr[i] *= 2       # Double the current
                arr[i + 1] = 0    # Replace next with 0
                i += 1            # Skip next as it's now 0
            i += 1

        # Step 2: Move all non-zero elements to the front
        result = []
        for num in arr:
            if num != 0:
                result.append(num)

        # Fill remaining positions with 0
        result += [0] * (n - len(result))
        return result



#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends