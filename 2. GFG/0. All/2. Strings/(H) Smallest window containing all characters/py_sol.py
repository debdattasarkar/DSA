class Solution:
    def smallestWindow(self, s, p):
        # code here
        n, m = len(s), len(p)
        if m > n:
            return ""

        # 1) Build required frequency and count how many distinct letters we need
        need = [0] * 26
        for ch in p:
            need[ord(ch) - 97] += 1
        required = sum(1 for x in need if x > 0)

        # 2) Sliding window state
        have = [0] * 26                   # counts in current window
        formed = 0                        # how many chars currently meet their need
        best_len = float('inf')
        best_l = 0
        l = 0

        # 3) Expand right pointer
        for r, ch in enumerate(s):
            ci = ord(ch) - 97
            have[ci] += 1
            # did we just satisfy a needed character?
            if need[ci] > 0 and have[ci] == need[ci]:
                formed += 1

            # 4) If all req'd letters are satisfied, shrink from left
            while formed == required:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l

                left_ci = ord(s[l]) - 97
                have[left_ci] -= 1
                # did we break the requirement for this char?
                if need[left_ci] > 0 and have[left_ci] < need[left_ci]:
                    formed -= 1
                l += 1

        return "" if best_len == float('inf') else s[best_l:best_l + best_len]
