#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        """
        Returns the exact count (no modulo) for n up to 30.
        Recurrence: f(n) = f(n-1) + f(n-2) + f(n-3)
        Base: f(0)=1, f(1)=1, f(2)=2
        """

        # ---------- Option 3 (enabled): Iterative with O(1) space ----------
        # Rationale: Most expected in interviews — linear time, constant space.
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        # rolling variables for f(n-3), f(n-2), f(n-1)
        a, b, c = 1, 1, 2  # f(0), f(1), f(2)
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c  # shift window and compute next tribonacci
        return c