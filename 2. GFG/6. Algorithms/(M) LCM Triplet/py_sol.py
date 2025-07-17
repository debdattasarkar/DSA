import math
class Solution:
    def lcm(self, a, b):
        return a * b // math.gcd(a, b)

    def lcm3(self, a, b, c):
        return self.lcm(a, self.lcm(b, c))
        
    def lcmTriplets(self, n):
        #code here
        # Special cases where n <= 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6

        # If n is odd, just take (n, n-1, n-2)
        if n % 2 != 0:
            return self.lcm3(n, n-1, n-2)
        else:
            # If n is even, we consider 3 possible combinations to avoid divisible by 2:
            # (n, n-1, n-3) avoids multiple even numbers
            # (n-1, n-2, n-3)
            # (n, n-1, n-2)
            return max(
                self.lcm3(n, n-1, n-3),
                self.lcm3(n-1, n-2, n-3),
                self.lcm3(n, n-1, n-2)
            )
            