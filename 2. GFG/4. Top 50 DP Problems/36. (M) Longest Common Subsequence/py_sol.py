class Solution:
    def lcs(self, s1, s2):
        # code here
        """
        Space-optimized bottom-up DP.
        Time:  O(n*m)
        Space: O(min(n, m))    # because we keep only previous and current rows
        """
        n, m = len(s1), len(s2)
        if n == 0 or m == 0:
            return 0

        # Always make 'b' the shorter string to minimize memory
        a, b = (s1, s2) if len(s1) >= len(s2) else (s2, s1)
        na, nb = len(a), len(b)

        prev = [0] * (nb + 1)            # dp for previous row  -> O(min(n,m)) space
        for i in range(1, na + 1):       # O(n)
            curr = [0] * (nb + 1)
            ai = a[i - 1]
            for j in range(1, nb + 1):   # O(m)
                if ai == b[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev[nb]