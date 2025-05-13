#User function Template for python3

class Solution:
    def nCr(self, n, r):
        # code here
        # Return 0 if r > n (invalid case)
        if r > n:
            return 0

        # Initialize DP array
        C = [0] * (r + 1)
        C[0] = 1  # Base case: nC0 = 1

        for i in range(1, n + 1):
            # Fill the array from right to left
            for j in range(min(i, r), 0, -1):
                C[j] = C[j] + C[j - 1]

        return C[r]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends