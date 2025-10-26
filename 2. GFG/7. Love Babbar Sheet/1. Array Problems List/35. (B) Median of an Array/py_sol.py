class Solution:
    def findMedian(self, arr):
        """
        Sort the array, then pick middle (or average of middles).
        Time  : O(n log n) for sort
        Space : O(1) extra if sort in-place
        """
        n = len(arr)
        arr.sort()  # in-place sort, O(n log n)

        mid = n // 2
        if n % 2 == 1:
            return float(arr[mid])                  # ensure float if needed
        else:
            # average of two middles; use .0 to keep float behavior
            return (arr[mid - 1] + arr[mid]) / 2.0