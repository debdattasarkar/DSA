class Solution:
	def getLPSLength(self, s):
		# Edge cases
        n = len(s)
        if n <= 1:
            return 0

        # Build LPS (prefix-function) array
        lps = [0] * n  # lps[i] = longest proper prefix == suffix for s[:i+1]
        length = 0     # current matched prefix length
        i = 1          # current index to fill

        # Time: O(n) — every char is processed with at most one fallback per mismatch
        # Space: O(n) for the LPS array (can be reduced to O(1) if you only keep 'length')
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # Fallback to the previous longest border
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # lps[-1] is the answer: longest proper prefix that's also a suffix for the whole string
        # Note: It can be equal to n only if whole string matches itself; but LPS builds proper borders, so lps[-1] <= n-1.
        return lps[-1]
		