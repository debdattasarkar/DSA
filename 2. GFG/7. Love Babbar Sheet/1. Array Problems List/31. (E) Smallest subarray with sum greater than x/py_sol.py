class Solution:
    def smallestSubWithSum(self, x, arr):
        """
        Sliding window for positive/non-negative arrays.
        Expand right to increase sum; while sum > x, shrink left to minimize length.
        Time : O(n)  -- each index enters/leaves the window at most once
        Space: O(1)
        Returns 0 if no subarray has sum > x (as per prompt).
        """
        n = len(arr)
        best_len = float('inf')
        window_sum = 0
        left = 0

        for right, val in enumerate(arr):     # expand window to the right
            window_sum += val

            # While we already exceed x, try to shrink from the left
            while window_sum > x:
                best_len = min(best_len, right - left + 1)
                window_sum -= arr[left]       # shrink window
                left += 1

        return 0 if best_len == float('inf') else best_len