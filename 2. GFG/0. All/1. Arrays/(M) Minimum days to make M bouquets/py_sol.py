class Solution:
    def minDaysBloom(self, arr, k, m):
        # Code here
        """
        Binary search on day D with a linear feasibility check.
        Time: O(n log(maxVal - minVal))
        Space: O(1)
        """
        n = len(arr)
        # Quick impossibility: not enough flowers overall
        if m * k > n:
            return -1

        low, high = min(arr), max(arr)

        def can_make(day):
            """
            Count how many bouquets we can form using
            only flowers with bloom day <= 'day'.
            Greedy O(n) scan; Space O(1).
            """
            run = bouquets = 0
            for a in arr:
                if a <= day:
                    run += 1
                    if run == k:
                        bouquets += 1
                        run = 0  # consume exactly k adjacent in this bouquet
                        if bouquets >= m:
                            return True
                else:
                    run = 0
            return False

        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if can_make(mid):
                ans = mid       # feasible -> try to minimize day
                high = mid - 1
            else:
                low = mid + 1   # infeasible -> need more days
        return ans