#User function Template for python3

class Solution:
    def encryptString(self, S):
        """
        Build the final (reversed) encoding directly:
          - Scan from right to left.
          - For each run of identical chars, append hex(count) + char.
        This preserves the order of hex digits for multi-digit counts.

        Time  : O(n)  (each character visited once)
        Space : O(n)  (output; list buffer used for O(n) join)
        """
        n = len(S)
        if n == 0:
            return ""

        out = []
        i = n - 1
        while i >= 0:
            j = i - 1
            # Count this backward run of S[i]
            while j >= 0 and S[j] == S[i]:
                j -= 1
            cnt = i - j                          # occurrences in this run
            out.append(format(cnt, "x"))         # lowercase hex, e.g. 16 -> "10"
            out.append(S[i])                     # then the character
            i = j
        return "".join(out)