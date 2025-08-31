# User function Template for python3
class Solution:
    # Function to return list containing first n Fibonacci numbers (0,1,1,2,3,...)
    def fibonacciNumbers(self, n):
        # Edge cases
        if n <= 0:
            return []              # no terms requested
        # Iterative generation
        res = []                   # O(n) for output
        a, b = 0, 1                # start at F0=0, F1=1
        for _ in range(n):         # O(n) time
            res.append(a)          # current term
            a, b = b, a + b        # next pair
        return res