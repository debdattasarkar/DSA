class Solution:
    def searchInsertK(self, arr, k):
        """
        Binary Search (Lower Bound):
        Return the first index i such that arr[i] >= k.
        If all elements < k, returns n.

        Time:  O(log n)
        Space: O(1)
        """
        n = len(arr)

        # Search in [left, right) => right is n (not n-1)
        left, right = 0, n

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < k:
                # k must be to the right of mid
                left = mid + 1
            else:
                # arr[mid] >= k, possible answer -> move left side
                right = mid

        # left is the first position where arr[left] >= k, or n if none
        return left