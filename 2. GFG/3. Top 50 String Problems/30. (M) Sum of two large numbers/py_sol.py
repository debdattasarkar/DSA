class Solution:
	def findSum(self, s1, s2):
		"""
        Add two non-negative integers given as decimal strings.
        Time:  O(n) where n = max(len(s1), len(s2))
        Space: O(n) for the output string
        
        Logic:
        - Start from the right end of both strings, add digit by digit with carry.
        - Build digits in reverse order, then reverse once at the end.
        - Strip leading zeros from final result unless the entire result is '0'.
        """
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        out = []  # collect digits in reverse

        while i >= 0 or j >= 0 or carry:
            d1 = ord(s1[i]) - 48 if i >= 0 else 0  # faster than int(s1[i])
            d2 = ord(s2[j]) - 48 if j >= 0 else 0
            total = d1 + d2 + carry
            out.append(chr((total % 10) + 48))
            carry = total // 10
            i -= 1
            j -= 1

        # reverse to normal order
        res = "".join(reversed(out))

        # remove leading zeros, but keep at least one '0'
        # (input assures non-negative numbers; both can be "0...0")
        k = 0
        while k + 1 < len(res) and res[k] == '0':
            k += 1
        return res[k:]