class Solution:
    def sort012(self, arr):
        """
        Dutch National Flag (single pass, in-place).
        Time  : O(n)   -- each index visited at most once
        Space : O(1)   -- constant extra pointers
        """
        low, mid, high = 0, 0, len(arr) - 1

        # Maintain invariants:
        # 0..low-1   -> all 0s
        # low..mid-1 -> all 1s
        # mid..high  -> unknown
        # high+1..n-1-> all 2s
        while mid <= high:
            if arr[mid] == 0:
                # put 0 into the 0s region, expand both low and mid
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # correct region, just advance
                mid += 1
            else:  # arr[mid] == 2
                # put 2 into the 2s region; do NOT advance mid yet
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr  # returning for convenience; in many platforms in-place is enough