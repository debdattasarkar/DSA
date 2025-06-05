#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n = len(arr)
        res = [1] * n
    
        # Step 1: Calculate prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= arr[i]  # Product of all elements before index i
    
        # Step 2: Multiply with suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix  # Multiply with product of all elements after index i
            suffix *= arr[i]
    
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends