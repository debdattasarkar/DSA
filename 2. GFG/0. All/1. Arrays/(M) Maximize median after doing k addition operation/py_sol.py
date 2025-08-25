class Solution:
    def maximizeMedian(self, arr, k):
        # code here
        # Sort to reason about the median and right half
        n = len(arr)
        arr.sort()

        # Check if target median 'median' is achievable with ≤ k increments
        def ok(median: int) -> bool:
            start = (n - 1) // 2  # index of middle for odd; left-middle for even

            # Even-length optimization: try to satisfy a+b >= 2*median cheaply
            if n % 2 == 0:
                a, b = arr[start], arr[start + 1]
                delta = median * 2 - (a + b)  # extra sum we must add to a and/or b
                if delta > k:
                    return False
                # If pushing only the smaller middle (a) is enough, we're done
                if b - a >= delta:
                    return True
                # Otherwise continue to general accumulation below

            # General case: raise all elements in the right half to >= median
            needed = 0
            for i in range(start, n):
                if arr[i] >= median:
                    break
                needed += median - arr[i]
                if needed > k:        # early stop
                    return False
            return needed <= k

        # Binary search the maximum feasible median
        lo = arr[(n - 1) // 2]       # current floor median
        hi = arr[-1] + k             # absolute max we could push to
        while lo < hi:
            mid = hi - (hi - lo) // 2  # upper mid for "max feasible" search
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo