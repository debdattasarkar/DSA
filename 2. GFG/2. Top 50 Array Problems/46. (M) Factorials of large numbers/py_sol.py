#User function Template for python3

class Solution:
    def factorial(self, n):
        """
        Build n! as a list of base-10 digits (MSD first).
        Representation: store digits LSB-first while multiplying, then reverse.

        Time:  O(n * D) where D ~ number of digits of n!  (≈ Θ(n log n)).
               For GFG constraints it's often summarized as O(n^2).
        Space: O(D) for the output digits (auxiliary outside result is O(1)).

        Returns: list[int] of digits, most-significant first.
        """
        # res holds digits least-significant-first during computation
        res = [1]  # 0! and 1! = 1

        # multiply res by every x in [2..n]
        for x in range(2, n + 1):
            carry = 0
            for i in range(len(res)):                  # O(current_digits)
                prod = res[i] * x + carry
                res[i] = prod % 10                     # write current digit
                carry = prod // 10                     # propagate carry
            while carry > 0:                            # append remaining carry
                res.append(carry % 10)
                carry //= 10

        res.reverse()  # convert to MSB-first for the return format
        return res