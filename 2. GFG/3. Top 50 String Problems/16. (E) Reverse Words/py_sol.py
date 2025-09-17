class Solution:
    def reverseWords(self, s):
        """
        Build the answer directly by scanning from right to left.
        Inserts a dot between words only (collapses multiple dots).
        Time  : O(n)
        Space : O(n) for the output buffer
        """
        n = len(s)
        out_parts = []
        i = n - 1

        while i >= 0:
            # skip any dots (handles multiple dots gracefully)
            while i >= 0 and s[i] == '.':
                i -= 1
            if i < 0:
                break

            # j is end of a word; find its start
            j = i
            while i >= 0 and s[i] != '.':
                i -= 1
            # s[i+1 : j+1] is one word
            out_parts.append(s[i+1 : j+1])

        # join found words with single dots (no leading/trailing/consecutive dots)
        return ".".join(out_parts)