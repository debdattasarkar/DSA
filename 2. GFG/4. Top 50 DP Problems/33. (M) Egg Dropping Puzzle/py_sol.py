#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self, n, k):
        """
        n = eggs, k = floors
        Idea: Find the smallest m such that F(m, n) >= k, where
              F(m, e) = F(m-1, e-1) + F(m-1, e) + 1.
        Time:  O(n * m)  <= O(n * k)
        Space: O(n)
        """
        if k == 0 or k == 1 or n == 1:
            # k=0 -> 0 moves; k=1 -> 1 move; 1 egg -> need linear checks (k moves)
            return k
        
        # dp[e] will hold F(m, e) for current m
        dp = [0] * (n + 1)   # dp[0] = 0 always; eggs are 1..n
        moves = 0
        
        # Keep increasing moves until we can cover k floors with n eggs
        while dp[n] < k:
            moves += 1
            # Update from high eggs to low to avoid overwriting dp[e-1] prematurely
            for e in range(n, 0, -1):
                dp[e] = dp[e] + dp[e - 1] + 1
                # dp[e] now equals F(moves, e)
        return moves