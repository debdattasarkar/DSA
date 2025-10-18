class Solution:
    def sort012(self, arr):
        """
        Dutch National Flag (single pass, in-place).
        Time  : O(n)   -- each index visited at most once
        Space : O(1)   -- constant extra pointers
        """
        left, mid, right = 0, 0, len(arr) - 1

        # Maintain invariants:
        # 0..left-1   -> all 0s
        # left..mid-1 -> all 1s
        # mid..right  -> unknown
        # right+1..n-1-> all 2s
        while mid <= right:
            if arr[mid] == 0:
                # put 0 into the 0s region, expand both left and mid
                arr[left], arr[mid] = arr[mid], arr[left]
                left += 1
                mid += 1
            elif arr[mid] == 1:
                # correct region, just advance
                mid += 1
            else:  # arr[mid] == 2
                # put 2 into the 2s region; do NOT advance mid yet
                arr[mid], arr[right] = arr[right], arr[mid]
                right -= 1
        return arr  # returning for convenience; in many platforms in-place is enough