class Solution:
    def checkPangram(self,s):
        """
        Time : O(n) — single pass
        Space: O(1) — at most 26 letters in the set
        """
        if len(s) < 26:                 # quick prune for English alphabet
            return False

        seen = set()                    # holds lowercase letters found (≤26)
        for ch in s:
            if 'A' <= ch <= 'Z':        # uppercase letter → normalize
                ch = chr(ord(ch) + 32)  # to lowercase
            if 'a' <= ch <= 'z':        # ignore non-letters defensively
                seen.add(ch)
                if len(seen) == 26:     # early exit
                    return True
        return len(seen) == 26