class Solution:
    def _build_lps(self, pattern: str):
        """
        Build LPS (Longest Prefix Suffix) array for KMP.
        lps[i] = length of the longest prefix of pattern that is also a suffix
                 for the substring pattern[0..i].

        Time:  O(m) where m = len(pattern)
        Space: O(m)
        """
        m = len(pattern)
        lps = [0] * m
        length = 0  # length of current longest prefix-suffix
        i = 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps
    def areRotations(self, s1, s2):
        """
        KMP-based rotation check:
            - Same as optimized, but perform substring search (s2 in s1+s1)
              manually using KMP to guarantee O(n).

        Time:  O(n)
        Space: O(n) for 'doubled' and lps.
        """
        if len(s1) != len(s2):
            return False

        doubled = s1 + s1
        text = doubled
        pattern = s2

        n = len(text)
        m = len(pattern)

        if m == 0:
            return True  # empty is substring

        lps = self._build_lps(pattern)

        i = j = 0  # i -> text index, j -> pattern index

        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == m:
                    return True  # found match
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return False