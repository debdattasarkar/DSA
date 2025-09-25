#User function Template for python3
from functools import lru_cache

class Solution:
    def optimalKeys(self, N):
        """
        Top-down with memo.
        Time:  O(N^2)  (each state tries k = 3..n)
        Space: O(N)    (recursion + memo)
        """

        @lru_cache(None)
        def f(n):
            if n <= 6:               # base: best is to type 'A'
                return n

            # Option 1: just type 'A'
            best = f(n - 1) + 1

            # Option 2: last k keystrokes = [Ctrl-A, Ctrl-C, (k-2)*Ctrl-V]
            # This multiplies the previous text by (k-1) copies.
            for k in range(3, n + 1):         # consume k keys for the final block
                best = max(best, f(n - k) * (k - 1))

            return best

        return f(N)