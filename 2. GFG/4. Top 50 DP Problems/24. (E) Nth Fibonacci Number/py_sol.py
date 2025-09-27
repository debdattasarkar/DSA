
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # Handle trivial bases in O(1)
        if n <= 1:
            return n

        # Maintain only the last two Fibonacci numbers
        a, b = 0, 1  # a = F(i-2), b = F(i-1)
        # Loop runs (n-1) times -> O(n) time, O(1) space
        for _ in range(2, n + 1):
            a, b = b, a + b  # advance the pair
        return b