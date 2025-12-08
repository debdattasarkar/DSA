from typing import List
class Solution:
    def matrixChainOrder(self, arr):
        """
        Bottom-up DP to print optimal parenthesization of matrix chain.

        arr: list of dimensions, length = n
             matrices: M1 (arr[0] x arr[1]),
                       M2 (arr[1] x arr[2]), ... ,
                       M(n-1) (arr[n-2] x arr[n-1])

        We compute:
            dp[i][j]    = minimum number of scalar multiplications needed
                          to multiply matrices Mi..Mj   (1-based indices)
            split[i][j] = index k where we split Mi..Mj for optimal cost

        Recurrence:
            dp[i][i] = 0
            dp[i][j] = min over k in [i..j-1] of:
                       dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]

        Then we recursively reconstruct the string using split[][].

        Complexity:
            Let m = n-1 = number of matrices.
            States: (i,j) with 1 <= i <= j <= m   -> O(m^2)
            For each state, we try O(m) splits.
            => Time  : O(m^3) ≈ O(n^3)
            => Space : O(m^2) for dp and split.
        """
        m = len(arr) - 1  # number of matrices
        if m <= 0:
            return ""

        # dp[i][j] and split[i][j] use 1-based indexing for convenience.
        # Allocate (m+1) x (m+1) tables.
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        split = [[0] * (m + 1) for _ in range(m + 1)]

        # Base: dp[i][i] = 0 already set (no cost to multiply one matrix)

        # chain_len = length of subchain (number of matrices in it)
        for chain_len in range(2, m + 1):  # from 2 matrices up to m
            for i in range(1, m - chain_len + 2):
                j = i + chain_len - 1
                dp[i][j] = float("inf")

                # Try all possible places to split the product Mi..Mj
                for k in range(i, j):
                    # Cost for (Mi..Mk) * (M(k+1)..Mj)
                    cost_left = dp[i][k]
                    cost_right = dp[k + 1][j]
                    cost_mult = arr[i - 1] * arr[k] * arr[j]
                    total_cost = cost_left + cost_right + cost_mult

                    if total_cost < dp[i][j]:
                        dp[i][j] = total_cost
                        split[i][j] = k

        # Helper function to rebuild the parenthesization string
        def build(i: int, j: int) -> str:
            """
            Recursively build the bracket string for Mi..Mj.

            - If i == j, just return the letter for Mi.
            - Else, wrap left and right parts in parentheses.
            """
            if i == j:
                # Mi is the (i-th) matrix => letter 'A' + (i-1)
                return chr(ord("A") + (i - 1))
            k = split[i][j]
            left_str = build(i, k)
            right_str = build(k + 1, j)
            return "(" + left_str + right_str + ")"

        return build(1, m)