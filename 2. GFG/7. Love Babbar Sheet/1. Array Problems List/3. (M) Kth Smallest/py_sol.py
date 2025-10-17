#User function Template for python3
import random
class Solution:
    def kthSmallest(self, arr,k):
        """
        Version 1 = 3-way (Dutch National Flag) partition.
        Quickselect with 3-way partition (Dutch National Flag).
        Average time: O(n), worst-case: O(n^2) -- mitigated by random pivot
        Space: O(1) extra (in-place)
        """
        n = len(arr)
        if not (1 <= k <= n):
            raise ValueError("k out of bounds")
        # We want 0-based index
        target = k-1
        left, right = 0, n-1
        
        while True:
            if left == right:
                return arr[left]
            # choose a random pivot to avoid adversarial worst cases
            pivot_idx = random.randint(left, right)
            pivot = arr[pivot_idx]
            # 3-way partition around pivot: < pivot | == pivot | > pivot
            pleft, i , pright = left, left, right
            while i <= pright:
                if arr[i] < pivot:
                    arr[pleft], arr[i] = arr[i], arr[pleft]
                    pleft += 1
                    i += 1
                elif arr[i] > pivot:
                    arr[i], arr[pright] = arr[pright], arr[i]
                    pright -= 1
                else: # equal
                    i += 1
            # Now:
            # arr[low:left]   < pivot
            # arr[left:right+1] == pivot
            # arr[right+1:high+1] > pivot
            if target < pleft:
                right = pleft - 1 # go left
            elif target > pright:
                left = pright + 1 # go right
            else:
                return arr[target] # inside the equal block → done