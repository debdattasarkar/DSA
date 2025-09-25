#User function Template for python3

class Solution:
    def longestSubstring(self, S):
        """
        Optimal prefix-parity solution.
        Time:  O(n * 26) ~ O(n)
        Space: O(2^26) worst-case if you used a fixed array; but we use a dict with at most n+1 keys.
        In practice: O(n).
        """
        n = len(S)
        earliest = {0: 0}  # mask -> earliest prefix index (before any char)
        mask = 0
        best = 0

        for i, ch in enumerate(S, 1):  # i is 1..n as prefix length
            bit = ord(ch) - 97
            mask ^= (1 << bit)         # update parity up to i

            # Case 1: same mask seen before => substring with all-even parity
            if mask in earliest:
                best = max(best, i - earliest[mask])
            else:
                earliest[mask] = i     # store earliest time we saw this mask

            # Case 2: differ by exactly one bit => exactly one odd letter
            # Try flipping each bit b
            m = mask
            for b in range(26):
                cand = m ^ (1 << b)
                if cand in earliest:
                    best = max(best, i - earliest[cand])

        return best