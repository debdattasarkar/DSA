#User function Template for python3

class Solution:
    def minTime (self, arr, k):
        #code here
        # Helper function to check if we can allocate boards to <= k painters
        def is_feasible(max_time):
            total, painters = 0, 1
            for length in arr:
                if total + length <= max_time:
                    total += length
                else:
                    painters += 1
                    total = length
            return painters <= k
        
        low = max(arr)           # A painter must at least paint the largest board
        high = sum(arr)         # One painter paints all
        result = high

        while low <= high:
            mid = (low + high) // 2
            if is_feasible(mid):
                result = mid
                high = mid - 1  # Try to minimize further
            else:
                low = mid + 1   # Increase limit
        
        return result
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        k = int(input())

        ob = Solution()
        print(ob.minTime(arr, k))

# } Driver Code Ends