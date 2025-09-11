#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        """
        Quickselect with 3-way partition (Dutch National Flag).
        Average time: O(n), worst-case: O(n^2) -- mitigated by random pivot
        Space: O(1) extra (in-place)
        """
        n = len(arr)
        if not (1 <= k <= n):
            raise ValueError("k out of bounds")

        # We want 0-based index
        target = k - 1
        lo, hi = 0, n - 1

        while True:
            if lo == hi:
                return arr[lo]

            # --- choose a random pivot to avoid adversarial worst cases
            pivot_idx = random.randint(lo, hi)
            pivot = arr[pivot_idx]

            # 3-way partition around pivot: < pivot | == pivot | > pivot
            lt, i, gt = lo, lo, hi
            while i <= gt:
                if arr[i] < pivot:
                    arr[lt], arr[i] = arr[i], arr[lt]
                    lt += 1; i += 1
                elif arr[i] > pivot:
                    arr[i], arr[gt] = arr[gt], arr[i]
                    gt -= 1
                else:  # equal
                    i += 1

            # Now:
            # arr[lo:lt]   < pivot
            # arr[lt:gt+1] == pivot
            # arr[gt+1:hi+1] > pivot

            if target < lt:
                hi = lt - 1                 # go left
            elif target > gt:
                lo = gt + 1                 # go right
            else:
                return arr[target]          # inside the equal block → done
        
