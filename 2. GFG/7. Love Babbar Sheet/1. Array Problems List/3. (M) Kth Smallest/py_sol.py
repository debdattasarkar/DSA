# User function Template for python3
import random

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
        low, high = 0, n - 1

        while True:
            if low == high:
                return arr[low]

            # --- choose a random pivot to avoid adversarial worst cases
            pivot_idx = random.randint(low, high)
            pivot = arr[pivot_idx]

            # 3-way partition around pivot: < pivot | == pivot | > pivot
            left, i, right = low, low, high
            while i <= right:
                if arr[i] < pivot:
                    arr[left], arr[i] = arr[i], arr[left]
                    left += 1; i += 1
                elif arr[i] > pivot:
                    arr[i], arr[right] = arr[right], arr[i]
                    right -= 1
                else:  # equal
                    i += 1

            # Now:
            # arr[low:left]   < pivot
            # arr[left:right+1] == pivot
            # arr[right+1:high+1] > pivot

            if target < left:
                high = left - 1                 # go left
            elif target > right:
                low = right + 1                 # go right
            else:
                return arr[target]          # inside the equal block → done
        
