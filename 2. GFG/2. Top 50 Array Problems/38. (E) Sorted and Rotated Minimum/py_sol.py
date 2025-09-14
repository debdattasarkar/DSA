#User function Template for python3

class Solution:
    def findMin(self, arr):
        """
        Optimized binary search: compare with right end.
        Distinct elements guaranteed.
        Time:  O(log n)
        Space: O(1)
        """
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            # If mid element is greater than rightmost,
            # the minimum is strictly to the right of mid.
            if arr[mid] > arr[r]:
                l = mid + 1
            else:
                # Minimum is at mid or in left part (including mid)
                r = mid
        return arr[l]