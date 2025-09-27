#User function Template for python3

class Solution:
    def minOperation(self, n):
        """
        Greedy backwards:
          - if n is even, the previous state must be n//2  (cheapest)
          - if n is odd,  the previous state must be n-1
        Stops at 0; counts steps.

        Time:  O(log n)    (each divide by 2 removes one bit; odd cases are O(popcount))
        Space: O(1)
        """
        steps = 0
        while n > 0:                 # loop runs ≈ bit_length(n) + popcount(n) times
            if n & 1:                # odd?
                n -= 1               # make it even: one operation
            else:
                n >>= 1              # divide by 2: one operation
            steps += 1
        return steps