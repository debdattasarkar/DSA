class Solution:
    def countRevPairs(self, arr):
        # Code here
        # Merge-sort based counter
        # Time: O(n log n), Space: O(n) for the temp array
        
        n = len(arr)
        tmp = [0] * n  # reuse a single temp buffer to reduce allocations

        def sort_and_count(lo, hi):
            # sorts arr[lo:hi] in place and returns the number of reverse pairs
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            cnt = sort_and_count(lo, mid) + sort_and_count(mid, hi)

            # Count cross pairs: left in [lo, mid), right in [mid, hi)
            j = mid
            for i in range(lo, mid):
                # move j while arr[i] > 2*arr[j]
                while j < hi and arr[i] > 2 * arr[j]:
                    j += 1
                cnt += (j - mid)  # all right elements before j worked for arr[i]

            # Merge step (stable)
            i, j, k = lo, mid, lo
            while i < mid and j < hi:
                if arr[i] <= arr[j]:
                    tmp[k] = arr[i]
                    i += 1
                else:
                    tmp[k] = arr[j]
                    j += 1
                k += 1
            # copy tails
            while i < mid:
                tmp[k] = arr[i]; i += 1; k += 1
            while j < hi:
                tmp[k] = arr[j]; j += 1; k += 1
            # write back
            arr[lo:hi] = tmp[lo:hi]
            return cnt

        return sort_and_count(0, n)