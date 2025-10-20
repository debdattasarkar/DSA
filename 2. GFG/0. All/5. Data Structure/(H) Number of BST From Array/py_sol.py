class Solution:
    def countBSTs(self, arr):
        """
        Strategy:
          1) Sort to get rank of each value -> L (#smaller), R (#greater).
          2) Precompute Catalan numbers up to n.
          3) Answer[i] = C[L] * C[R].

        Time  : O(n log n) for sort + O(n^2) for Catalan DP (or O(n) if using direct formula w/ big ints)
        Space : O(n)
        """
        n = len(arr)
        if n == 0:
            return []

        # 1) ranks
        sorted_vals = sorted(arr)                                 # O(n log n)
        rank = {v: i for i, v in enumerate(sorted_vals)}          # O(n)

        # 2) Catalan numbers up to n
        C = [0] * (n + 1)
        C[0] = 1
        for k in range(1, n + 1):                                 # O(n^2)
            total = 0
            # Ck = sum_{i=0..k-1} (Ci * C_{k-1-i})
            for i in range(k):
                total += C[i] * C[k - 1 - i]
            C[k] = total

        # 3) compute answers
        ans = []
        for x in arr:                                             # O(n)
            L = rank[x]
            R = n - 1 - L
            ans.append(C[L] * C[R])
        return ans