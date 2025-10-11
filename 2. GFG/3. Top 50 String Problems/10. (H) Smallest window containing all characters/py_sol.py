class Solution:
    def smallestWindow(self, s, p):
        """
        Sliding-window with fixed-size counts (lowercase only).
        missing = total number of characters from p still needed across duplicates.
        Time  : O(n)
        Space : O(1)  (26-sized arrays)
        """
        n, m = len(s), len(p)
        if m == 0:
            return ""
        if m > n:
            return ""

        def idx(c):  # map 'a'..'z' -> 0..25
            return ord(c) - 97

        need = [0] * 26
        for ch in p:                      # O(m)
            need[idx(ch)] += 1

        have = [0] * 26                   # window counts
        missing = m                       # how many total chars still needed (with duplicates)

        best_len = float("inf")
        best_l = 0
        l = 0

        for r, ch in enumerate(s):        # O(n)
            r_id = idx(ch)
            have[r_id] += 1
            if have[r_id] <= need[r_id]:
                # this char satisfied one required instance
                missing -= 1

            # when window covers all required characters, shrink from left
            while missing == 0:
                # update best (tie-break by earliest start)
                curr_len = r - l + 1
                if curr_len < best_len or (curr_len == best_len and l < best_l):
                    best_len = curr_len
                    best_l = l

                # try removing s[l]
                l_id = idx(s[l])
                have[l_id] -= 1
                if have[l_id] < need[l_id]:
                    # we just made the window invalid; need to expand again
                    missing += 1
                l += 1

        return "" if best_len == float("inf") else s[best_l:best_l + best_len]
