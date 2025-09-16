#User function template for Python 3

class Solution:
    def convertRoman(self, n):
        """
        Greedy over descending (value, symbol) pairs.
        Time  : O(1)   (constant-sized list; at most ~15 appends)
        Space : O(1)   (output excluded)
        """
        vals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"), (1, "I")
        ]
        out = []
        for v, sym in vals:
            if n == 0:
                break
            # how many times current value fits
            cnt = n // v                     # O(1)
            if cnt:
                out.append(sym * cnt)        # O(1) small constant
                n -= v * cnt                 # O(1)
        return "".join(out)