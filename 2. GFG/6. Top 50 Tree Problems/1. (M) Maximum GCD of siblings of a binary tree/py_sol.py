#User function Template for python3
from math import gcd
from collections import defaultdict

class Solution:
    def maxBinTreeGCD(self, arr, N):
        """
        Time  : O(E) ~ O(N) because we touch each edge once and at most compute a few gcds.
        Space : O(E) to store parent->children lists.
        """
        if not arr:
            return 0
        
        # 1) Build parent -> list of children
        children = defaultdict(list)
        for p, c in arr:
            children[p].append(c)
        
        # 2) For each parent, if >= 2 children, compute best sibling gcd
        ans = 0
        for p, kids in children.items():
            if len(kids) >= 2:
                # Normally, binary tree => len(kids) <= 2
                # Be robust if more appear: compute the best pairwise gcd.
                if len(kids) == 2:
                    ans = max(ans, gcd(kids[0], kids[1]))
                else:
                    # Robustness: best pairwise gcd among the children (rare if input breaks binary property)
                    # O(k^2) where k is tiny in practice.
                    k = len(kids)
                    for i in range(k):
                        for j in range(i + 1, k):
                            ans = max(ans, gcd(kids[i], kids[j]))
        return ans