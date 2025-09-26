#User function Template for python3

class Solution:
    def cutRod(self, price):
        """
        Unbounded knapsack / rod cutting.
        best[L] = max_{1<=cut<=L} (price[cut-1] + best[L-cut])

        Time  : O(n^2)
        Space : O(n)
        """
        n = len(price)
        best = [0] * (n + 1)   # best[0]=0

        for L in range(1, n + 1):           # increasing length
            max_val = 0
            # try first cut of every allowable length
            for cut in range(1, L + 1):     # O(L)
                max_val = max(max_val, price[cut - 1] + best[L - cut])
            best[L] = max_val

        return best[n]