class Solution:
    def countSetBits(self,n):
        """
        Optimized method using highest power of 2 <= n and recursion.

        Recurrence:
            f(n) = x * 2^(x-1) + (n - 2^x + 1) + f(n - 2^x)
        where 2^x <= n < 2^(x+1)

        Time  : O(log n)  (each recursive step reduces n roughly by half)
        Space : O(log n) recursion stack, O(1) extra otherwise
        """

        # Base case: no numbers => no set bits
        if n == 0:
            return 0

        # ---------- Step 1: find highest power of 2 <= n ----------
        # We find x such that 2^x <= n < 2^(x+1)
        x = self._highest_power_exponent(n)
        power_of_two = 1 << x  # 2^x

        # ---------- Step 2: count bits from 1 to (2^x - 1) ----------
        # In this range, each of x lower bits is set exactly 2^(x-1) times
        bits_before_power = x * (1 << (x - 1)) if x > 0 else 0

        # ---------- Step 3: count MSB bits for numbers from 2^x to n ----------
        # All numbers in [2^x, n] have MSB (bit x) set
        msb_bits = n - power_of_two + 1

        # ---------- Step 4: recursively count lower bits contribution ----------
        # Map [2^x, n] to [0, n - 2^x] and reuse f()
        remaining = n - power_of_two
        lower_bits = self.countSetBits(remaining)

        # Total = contribution from:
        # (1) 1..(2^x-1)
        # (2) MSBs in 2^x..n
        # (3) lower bits in 2^x..n (same as f(remaining))
        return bits_before_power + msb_bits + lower_bits

    def _highest_power_exponent(self, n: int) -> int:
        """
        Returns the exponent x such that 2^x <= n < 2^(x+1).

        Simple loop: O(log n) but called only once per recursion level.
        """
        x = 0
        while (1 << (x + 1)) <= n:
            x += 1
        return x