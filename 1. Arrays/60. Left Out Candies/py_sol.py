#User function Template for python3
class Solution:
    def leftCandies(self, n, m):
        #code
        low, high = 0, m
        # Binary search for max complete rounds
        while low <= high:
            mid = (low + high) // 2
            # Total candies used in mid rounds
            total = mid * n * (n + 1) // 2
            if total <= m:
                low = mid + 1
            else:
                high = mid - 1
        
        # Deduct candies used in full `high` rounds
        used = high * n * (n + 1) // 2
        m -= used
        
        # Now simulate one last incomplete round
        for i in range(1, n + 1):
            if m >= i:
                m -= i
            else:
                break
        return m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Position this line where user code will be pasted.
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.leftCandies(n, m)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends