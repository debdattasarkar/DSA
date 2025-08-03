#User function Template for python3
class Solution:
    def countWays(self, s):
        # code here
        n = len(s)
        operands = (n + 1) // 2
        
        # dpTrue[i][j] = number of ways subexpression i to j evaluates to True
        # dpFalse[i][j] = number of ways subexpression i to j evaluates to False
        dpTrue = [[0] * operands for _ in range(operands)]
        dpFalse = [[0] * operands for _ in range(operands)]
        
        # Initialize for single operands (length 1)
        for i in range(operands):
            if s[2 * i] == 'T':
                dpTrue[i][i] = 1  # One way to be True
                dpFalse[i][i] = 0
            else:
                dpTrue[i][i] = 0
                dpFalse[i][i] = 1  # One way to be False
        
        # len = length of subexpression in terms of number of operands
        for length in range(2, operands + 1):  # Start from length 2
            for i in range(operands - length + 1):  # Start index
                j = i + length - 1  # End index
        
                for k in range(i, j):  # Try all partitions
                    op = s[2 * k + 1]  # Operator between k and k+1
        
                    lt = dpTrue[i][k]      # Left True
                    lf = dpFalse[i][k]     # Left False
                    rt = dpTrue[k + 1][j]  # Right True
                    rf = dpFalse[k + 1][j] # Right False
        
                    # Apply operator logic to combine counts
                    if op == '&':
                        dpTrue[i][j] += lt * rt
                        dpFalse[i][j] += lt * rf + lf * rt + lf * rf
                    elif op == '|':
                        dpTrue[i][j] += lt * rt + lt * rf + lf * rt
                        dpFalse[i][j] += lf * rf
                    elif op == '^':
                        dpTrue[i][j] += lt * rf + lf * rt
                        dpFalse[i][j] += lt * rt + lf * rf
        
        # Final result is total ways full expression can be True
        return dpTrue[0][operands - 1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        print(Solution().countWays(s))
        print("~")

# } Driver Code Ends