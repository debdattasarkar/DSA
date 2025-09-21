class Solution:
    def multiplyStrings(self, s1, s2):
        # Handle sign first
        neg = (s1[0] == '-') ^ (s2[0] == '-')
        if s1[0] in '+-': s1 = s1[1:]
        if s2[0] in '+-': s2 = s2[1:]

        # Strip leading zeros
        s1 = s1.lstrip('0') or '0'
        s2 = s2.lstrip('0') or '0'
        if s1 == '0' or s2 == '0':
            return '0'

        n, m = len(s1), len(s2)
        res = [0] * (n + m)  # result digits (base 10)

        # Convert char -> digit via ord (no int() on whole string)
        def dig(c): return ord(c) - 48  # ord('0') == 48

        # Multiply like grade-school (right-to-left)
        for i in range(n - 1, -1, -1):
            d1 = dig(s1[i])
            carry = 0
            for j in range(m - 1, -1, -1):
                d2 = dig(s2[j])
                # sum existing + this partial + carry
                total = res[i + j + 1] + d1 * d2 + carry
                res[i + j + 1] = total % 10
                res[i + j]     += total // 10  # carry flows to the left

        # Convert to string and strip leading zeros
        # (there might still be one at res[0])
        i = 0
        while i < len(res) - 1 and res[i] == 0:
            i += 1
        ans = ''.join(str(d) for d in res[i:])
        return ('-' + ans) if neg else ans