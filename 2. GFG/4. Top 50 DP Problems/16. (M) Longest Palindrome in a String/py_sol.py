class Solution:
    def getLongestPal(self, s):
        """
        Manacher's algorithm.
        Time  : O(n)
        Space : O(n)
        """
        if len(s) <= 1:
            return s

        # Transform: "^#a#b#...#z#$"
        T = ['^']
        for ch in s:
            T += ['#', ch]
        T += ['#', '$']
        T = ''.join(T)
        nT = len(T)

        P = [0] * nT  # radius array
        C = R = 0     # current center, right boundary
        best_len = 0
        best_start = 0  # in original string indices

        for i in range(1, nT - 1):
            mirror = 2 * C - i
            if i < R:
                P[i] = min(R - i, P[mirror])
            # expand around i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            # update center if expanded beyond R
            if i + P[i] > R:
                C, R = i, i + P[i]

            # convert radius in T to [l..r] in s
            length = P[i]                # length in transformed chars
            start = (i - length) // 2    # starting index in original s
            # length in original string:
            plen = length

            # strictly longer -> update, tie -> keep earlier start
            if plen > best_len or (plen == best_len and start < best_start):
                best_len = plen
                best_start = start

        return s[best_start: best_start + best_len]