class Solution:
    def countSubstr (self, s, k):
        if k <= 0:
            return 0
        return self._at_most(s, k) - self._at_most(s, k - 1)

    def _at_most(self, s, K):
        if K < 0:
            return 0
        n = len(s)
        L = 0
        freq = [0] * 26      # faster than dict for 'a'..'z'
        distinct = 0
        total = 0

        for R, ch in enumerate(s):
            idx = ord(ch) - 97
            if freq[idx] == 0:
                distinct += 1
            freq[idx] += 1

            # shrink until ≤ K distinct
            while distinct > K:
                idxL = ord(s[L]) - 97
                freq[idxL] -= 1
                if freq[idxL] == 0:
                    distinct -= 1
                L += 1

            # all substrings ending at R and starting from any i in [L..R] are valid
            total += (R - L + 1)

        return total