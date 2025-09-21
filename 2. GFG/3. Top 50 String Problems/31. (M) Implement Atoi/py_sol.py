class Solution:
    def myAtoi(self, s):
        """
        Optimal interview version:
        - Same parsing, but we PRE-CHECK overflow before multiplying by 10 and adding digit.
        - This mirrors what you'd do in C++/Java.
        Time:  O(n)
        Space: O(1)
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        i, n = 0, len(s)
        # 1) skip spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2) sign
        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        # 3) digits with pre-check overflow
        res = 0
        read_any = False
        while i < n and '0' <= s[i] <= '9':
            read_any = True
            d = ord(s[i]) - ord('0')

            # If next step would overflow INT_MAX, clamp immediately
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and d > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            res = res * 10 + d
            i += 1

        if not read_any:
            return 0

        res *= sign
        # (res is guaranteed in range due to pre-check)
        return res