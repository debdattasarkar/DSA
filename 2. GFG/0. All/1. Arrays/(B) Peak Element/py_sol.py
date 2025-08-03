class Solution:   
    def peakElement(self,arr):
        # Code here
        n = len(arr)
        start, end = 0, n - 1

        # Step 1: Binary Search Loop
        # Time Complexity: O(log n) — halves the search space each iteration
        # Space Complexity: O(1) — constant space used
        while start <= end:
            mid = (start + end) // 2

            # Step 2: Define neighbors with edge protection
            # Time: O(1) per access
            left = float('-inf') if mid == 0 else arr[mid - 1]
            right = float('-inf') if mid == n - 1 else arr[mid + 1]

            # Step 3: Peak Check
            if arr[mid] >= left and arr[mid] >= right:
                return mid  # Found a peak

            # Step 4: Decide search direction
            elif arr[mid] < right:
                start = mid + 1  # Move to right half
            else:
                end = mid - 1    # Move to left half

        return -1  # This shouldn't happen as a peak is guaranteed
