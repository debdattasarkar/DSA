class Solution:
    def quickSort(self, arr, low, high):
        """
        Recursive QuickSort using Lomuto partition (pivot = arr[high]).
        Time (avg): O(n log n); Worst: O(n^2)
        Space: recursion stack O(log n) avg, O(n) worst
        """
        if low < high:
            p = self.partition(arr, low, high)  # pivot index in correct place
            self.quickSort(arr, low, p - 1)     # sort left side
            self.quickSort(arr, p + 1, high)    # sort right side

    def partition(self, arr, low, high):
        """
        Lomuto partition:
          - arr[high] is pivot
          - i separates (≤ pivot) and (> pivot)
        Returns: final pivot index
        Time: O(high - low + 1), Space: O(1)
        """
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):         # scan all but the pivot
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        # place pivot after the last element ≤ pivot
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1