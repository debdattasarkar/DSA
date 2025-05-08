#User function Template for python3

class Solution:
    def countZeroes(self, arr):
        # code here
        n = len(arr)
        low, high = 0, n - 1
        first_zero = -1

        # Binary search for first 0
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == 0:
                first_zero = mid
                high = mid - 1  # search left half
            else:
                low = mid + 1

        # If no 0's
        if first_zero == -1:
            return 0
        return n - first_zero


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countZeroes(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends