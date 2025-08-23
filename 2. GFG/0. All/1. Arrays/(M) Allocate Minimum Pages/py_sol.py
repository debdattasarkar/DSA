class Solution:
    def findPages(self, arr, k):
        # code here
        """
        Time:  O(n log(sum(arr)))   where n = len(arr)
        Space: O(1)
        """
        n = len(arr)
        # Edge cases
        if k > n:
            return -1
        if k == 1:
            return sum(arr)
        if k == n:
            return max(arr)

        def can_distribute(cap: int) -> bool:
            """Return True if we can assign books to <= k students
            such that no one gets more than 'cap' pages."""
            students = 1
            cur = 0
            for pages in arr:
                if pages > cap:  # single book exceeds cap -> impossible
                    return False
                if cur + pages <= cap:
                    cur += pages
                else:
                    students += 1
                    cur = pages
                    if students > k:
                        return False
            return True

        lo, hi = max(arr), sum(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_distribute(mid):
                hi = mid      # feasible -> try smaller cap
            else:
                lo = mid + 1  # infeasible -> need larger cap
        return lo