class Solution:
    def romanToDecimal(self, s): 
        """
        Scan left→right. If current < next, subtract; else add.
        Time : O(n)  (single pass)
        Space: O(1)  (constant mapping)
        """
        val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        n = len(s)
        total = 0
        for i, ch in enumerate(s):
            v = val[ch]                     # O(1)
            # If a larger value follows, this is a subtractive position.
            if i + 1 < n and v < val[s[i + 1]]:
                total -= v
            else:
                total += v
        return total