class Solution:
    def search(self, pat, txt):
        """
        KMP pattern search.
        Time:  O(n + m)  (build LPS in O(m), scan text in O(n))
        Space: O(m)      (LPS array)
        Returns: list of 0-based starting indices where pat occurs in txt
        """
        n, m = len(txt), len(pat)
        if m == 0 or m > n:
            return []  # by constraints m >= 1, but keep safe

        # -------- build LPS (Longest Prefix Suffix) for 'pat' --------
        lps = [0] * m
        # len_ = length of the current longest prefix-suffix
        len_ = 0
        i = 1
        # Build LPS in O(m)
        while i < m:
            if pat[i] == pat[len_]:
                len_ += 1
                lps[i] = len_
                i += 1
            else:
                if len_ != 0:
                    len_ = lps[len_ - 1]  # fallback; do not increment i
                else:
                    lps[i] = 0
                    i += 1

        # -------- scan text with reuse via LPS --------
        res = []
        i = j = 0  # i -> txt, j -> pat
        # O(n) scan
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == m:
                    # Found an occurrence ending at i-1
                    res.append(i - m)   # 0-based start index
                    j = lps[j - 1]      # continue to find next match (overlaps allowed)
            else:
                if j != 0:
                    j = lps[j - 1]      # reuse previous prefix
                else:
                    i += 1              # no partial match to reuse; advance text

        return res