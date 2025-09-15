#User function Template for python3
from collections import defaultdict
class Solution:
    def getSubstringWithEqual012(self, Str):
        """
        Count substrings with equal #0, #1, #2 using prefix-difference hashing.
        Let d1 = c0 - c1, d2 = c0 - c2. Same (d1,d2) seen earlier ⇒
        substring between positions has Δ0=Δ1=Δ2.
        Time : O(N)  (single pass; O(1) dict ops amortized)
        Space: O(N)  (map stores up to N distinct pairs)
        """
        c0 = c1 = c2 = 0
        freq = defaultdict(int)
        freq[(0, 0)] = 1     # empty prefix
        ans = 0

        for ch in Str:
            if ch == '0':
                c0 += 1
            elif ch == '1':
                c1 += 1
            else:  # '2'
                c2 += 1

            d1 = c0 - c1
            d2 = c0 - c2

            # All earlier occurrences of (d1,d2) form a valid substring ending here
            ans += freq[(d1, d2)]
            freq[(d1, d2)] += 1

        return ans