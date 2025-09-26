class Solution:
    def minTime (self, arr, k):
        """
        Binary search the minimal feasible 'max load' (time).
        Predicate: can we partition arr into at most k contiguous groups
                    so that each group's sum <= T ?
        Time : O(n * log(sum(arr)))     -- predicate is O(n), ~log range checks
        Space: O(1)
        """
        n = len(arr)
        if n == 0:
            return 0
        # If painters >= boards, each painter can take at most one board
        # -> the time is the largest board.
        if k >= n:
            return max(arr)

        lo, hi = max(arr), sum(arr)

        def feasible(T: int) -> bool:
            painters = 1
            curr = 0
            for L in arr:
                if L > T:             # single board too large
                    return False
                if curr + L <= T:     # keep filling current painter
                    curr += L
                else:                 # need a new painter
                    painters += 1
                    curr = L
                    if painters > k:  # early exit
                        return False
            return True

        # standard lower-bound binary search
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo