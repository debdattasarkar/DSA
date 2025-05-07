class Solution:
    def transitionPoint(self, arr): 
        # Code here
        n = len(arr)
        low = 0
        high = n - 1
        result = -1  # Default if 1 is not found

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == 1:
                result = mid         # potential first 1 found
                high = mid - 1       # search left half
            else:
                low = mid + 1        # search right half

        return result


#{ 
 # Driver Code Starts
#driver code
if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.transitionPoint(arr))

        print("~")

# } Driver Code Ends