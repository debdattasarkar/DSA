class Solution:
    def combinationSum(self, n, k):
        # Results will hold all valid combinations
        res, path = [], []

        # Arithmetic helpers for pruning
        def min_sum(start, r):
            # Sum of r smallest numbers starting from `start`
            # = r/2 * [2*start + (r-1)]
            return r * (2 * start + (r - 1)) // 2

        def max_sum(r):
            # Sum of r largest numbers from 1..9
            # = r/2 * [9 + (10 - r)] = r/2 * (19 - r)
            return r * (19 - r) // 2

        def dfs(start, k_left, remain):
            # If we've picked k numbers, check if the sum hits exactly
            if k_left == 0:
                if remain == 0:
                    res.append(path.copy())
                return

            # 1) Not enough numbers left in 1..9 (from 'start' onward)
            if k_left > 10 - start:
                return

            # 2) Lower bound prune
            if remain < min_sum(start, k_left):
                return

            # 3) Upper bound prune
            if remain > max_sum(k_left):
                return

            # Try each next number once, in increasing order
            for x in range(start, 10):  # numbers 1..9
                if x > remain:
                    break  # 4) monotonic break
                path.append(x)
                dfs(x + 1, k_left - 1, remain - x)
                path.pop()  # backtrack

        dfs(1, k, n)
        return res