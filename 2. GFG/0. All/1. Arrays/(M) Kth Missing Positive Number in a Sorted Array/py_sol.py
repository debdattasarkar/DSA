class Solution:
    def kthMissing(self, arr, k):
        """
        Binary search for the smallest index idx with missing(idx) >= k,
        where missing(i) = arr[i] - (i + 1).

        Time:  O(log n)
        Space: O(1)
        """
        n = len(arr)
        # Total missing up to the last element
        total_missing = arr[-1] - n
        if total_missing < k:
            # k-th missing is beyond the last array element
            return arr[-1] + (k - total_missing)

        # Find first index with missing(idx) >= k (lower_bound)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] - (mid + 1) >= k:
                hi = mid
            else:
                lo = mid + 1

        # lo is that first index; answer is k + lo (proof in explanation)
        return k + lo