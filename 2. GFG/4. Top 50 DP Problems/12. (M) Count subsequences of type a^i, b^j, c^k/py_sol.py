#User function Template for python3

class Solution:
    def fun(self,s):
        """
        Count subsequences of type a^i b^j c^k (i,j,k >= 1)
        Using 3 running counters.
        Time : O(n)
        Space: O(1)
        """
        MOD = 1_000_000_007
        A = AB = ABC = 0

        for ch in s:
            if ch == 'a':
                # Existing a^+ subsequences: choose or skip this 'a' (2*A)
                # Start a new subsequence with just this 'a' (+1)
                A = (2 * A + 1) % MOD
            elif ch == 'b':
                # Existing a^+b^+ subsequences: choose or skip this 'b' (2*AB)
                # Extend any a^+ into a^+b^+ by taking this 'b' (+A)
                AB = (2 * AB + A) % MOD
            elif ch == 'c':
                # Existing a^+b^+c^+ subsequences: choose/skip this 'c' (2*ABC)
                # Extend any a^+b^+ into a^+b^+c^+ by taking this 'c' (+AB)
                ABC = (2 * ABC + AB) % MOD
            else:
                # other letters don't matter for this pattern
                pass

        return ABC % MOD