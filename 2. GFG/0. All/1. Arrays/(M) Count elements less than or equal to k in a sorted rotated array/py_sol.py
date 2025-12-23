class Solution:
    def countLessEqual(self, arr, x):
        #code here
        n = len(arr)
        if n == 0:
            return 0

        # ---------- Step 1: Find pivot (min element index) ----------
        # Time: O(log n), Space: O(1)
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        pivot = low  # smallest element index

        # ---------- Step 2: Count <= x in sorted segments ----------
        # upper_bound in [left..right] => count of <= x in that segment
        def upper_bound_in_range(left, right, target):
            if left > right:
                return 0
            lo, hi = left, right
            ans = right + 1  # default: all <= target
            while lo <= hi:
                m = (lo + hi) // 2
                if arr[m] > target:
                    ans = m
                    hi = m - 1
                else:
                    lo = m + 1
            return ans - left

        # Segment1: [pivot .. n-1]
        count_right = upper_bound_in_range(pivot, n - 1, x)
        # Segment2: [0 .. pivot-1]
        count_left = upper_bound_in_range(0, pivot - 1, x)

        return count_left + count_right