# User function Template for python3

class Solution:
    
    # ----- helper: find with path compression -----
    def _find(self, x, par):
        """
        Finds the root (representative) of x.
        Path compression makes future finds almost O(1).
        Amortized time: O(α(N)).
        """
        if par[x] != x:
            par[x] = self._find(par[x], par)  # compress path
        return par[x]
    
    # Function to merge two nodes a and b.
    def union_(self, a, b, par, rank1):
        """
        Union by rank:
        - Attach the lower-rank tree under the higher-rank tree.
        - If ranks equal, pick one as root and increment its rank.
        
        Amortized time per union: O(α(N)), space: O(1) extra.
        """
        ra = self._find(a, par)
        rb = self._find(b, par)
        if ra == rb:
            return  # already in same set
        
        # attach smaller-rank root under larger-rank root
        if rank1[ra] < rank1[rb]:
            par[ra] = rb
        elif rank1[rb] < rank1[ra]:
            par[rb] = ra
        else:
            # ranks equal: pick one root (say ra), increase its rank
            par[rb] = ra
            rank1[ra] += 1
    
    # Function to check whether 2 nodes are connected or not.
    def isConnected(self, x, y, par, rank1):
        """
        Connected iff their roots are equal.
        Each find is amortized O(α(N)).
        """
        return 1 if self._find(x, par) == self._find(y, par) else 0
