#User function Template for python3

class Solution:
    def isdivisible7(self, num):
        """
        Stream the digits and keep a running remainder modulo 7.
        Time  : O(n) where n = len(num)
        Space : O(1)
        """
        r = 0
        for ch in num:
            # convert char to digit
            d = ord(ch) - ord('0')      # O(1)
            r = (r * 10 + d) % 7        # O(1)
        return 1 if r == 0 else 0