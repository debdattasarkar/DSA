class Solution:
    def minWindow(self, s1, s2):
        n, m = len(s1), len(s2)
        if m == 0:
            return ""
        if n < m:
            return ""

        best_start = -1
        best_len = float("inf")

        i = 0  # pointer for s1
        while i < n:
            # ---------- Forward: find an end where s2 fully matches ----------
            j = 0  # pointer for s2
            while i < n:
                if s1[i] == s2[j]:
                    j += 1
                    if j == m:   # matched all of s2
                        break
                i += 1

            if j < m:
                break  # no more possible matches

            end = i  # s1[end] is where we completed matching s2

            # ---------- Backward: shrink to minimum start for this end ----------
            j = m - 1
            while j >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                i -= 1

            start = i + 1  # minimal start index for this window

            window_len = end - start + 1
            if window_len < best_len:
                best_len = window_len
                best_start = start

            # ---------- Move i to next position after start to search next window ----------
            i = start + 1

        if best_start == -1:
            return ""
        return s1[best_start:best_start + best_len]