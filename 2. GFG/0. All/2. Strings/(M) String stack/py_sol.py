class Solution:
    def stringStack(self, pat, tar):
        n, m = len(pat), len(tar)
        if m == 0:
            return True  # empty target is always possible

        # Required parity for i1:
        last_parity = (n - 1) & 1
        first_parity = last_parity if (m & 1) else (last_parity ^ 1)

        j = 0  # how many letters of tar matched
        for i, c in enumerate(pat):
            if j < m:
                needed_parity = first_parity ^ (j & 1)  # alternate parity
                if c == tar[j] and ((i & 1) == needed_parity):
                    j += 1

        # All matched? If yes, tail parity is already satisfied by construction.
        return j == m