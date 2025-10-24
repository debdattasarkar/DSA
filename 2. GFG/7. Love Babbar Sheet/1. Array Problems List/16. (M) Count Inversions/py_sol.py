class Solution:
    def inversionCount(self, arr):
        """
        Count inversions using merge-sort based counting.
        Time:  O(n log n)
        Space: O(n) extra for temp arrays
        """
        n = len(arr)
        if n <= 1:
            return 0

        # Helper: merge two sorted slices arr[l:m+1] and arr[m+1:r], count cross inversions
        def merge_and_count(a, l, m, r, buf):
            i, j, k = l, m + 1, l  # i->left, j->right, k->buf index
            inv = 0

            # Merge in ascending order; count inversions when left[i] > right[j]
            while i <= m and j <= r:
                if a[i] <= a[j]:
                    buf[k] = a[i]
                    i += 1
                else:
                    # a[i] > a[j] → all remaining left elements [i..m] are > a[j]
                    buf[k] = a[j]
                    inv += (m - i + 1)   # add how many are left in left half
                    j += 1
                k += 1

            # Copy leftovers (no new inversions because halves are sorted)
            while i <= m:
                buf[k] = a[i]; i += 1; k += 1
            while j <= r:
                buf[k] = a[j]; j += 1; k += 1

            # Write merged back to original array slice
            for t in range(l, r + 1):
                a[t] = buf[t]

            return inv

        # Recursive divide & conquer
        def sort_and_count(a, l, r, buf):
            if l >= r:
                return 0
            m = (l + r) // 2
            inv = 0
            inv += sort_and_count(a, l, m, buf)        # left inversions
            inv += sort_and_count(a, m + 1, r, buf)    # right inversions
            inv += merge_and_count(a, l, m, r, buf)    # cross inversions during merge
            return inv

        buffer = [0] * n  # O(n) temp
        return sort_and_count(arr, 0, n - 1, buffer)