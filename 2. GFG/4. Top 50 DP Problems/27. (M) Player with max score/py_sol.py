#User function Template for python3

class Solution:
    def is1winner (self, N, arr):
        """
        Returns True if Player 1 can ensure a score >= Player 2 (tie counts as a win).
        DP state: F(i,j) = best score difference current player can achieve on arr[i..j].
        Transition: F(i,j) = max(arr[i] - F(i+1,j), arr[j] - F(i,j-1)).
        Time: O(N^2), Space: O(N).
        """
        # 1-D DP along diagonals:
        # dp[j] holds F(i, j) for current i (looping i from N-2 downto 0, j from i+1..N-1)
        dp = arr[:]  # Base: F(j,j) = arr[j]
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N):
                take_left  = arr[i] - dp[j]       # arr[i] - F(i+1, j)
                take_right = arr[j] - dp[j - 1]   # arr[j] - F(i,   j-1)
                dp[j] = max(take_left, take_right)
        # Tie counts as a win for Player 1 on this platform
        return dp[N - 1] >= 0