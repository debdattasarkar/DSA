class Solution:
    def sort012(self, arr):
        """
        Dutch National Flag (DNF) partitioning.
        Invariants during the loop:
          [0..low-1]   -> 0s
          [low..mid-1] -> 1s
          [mid..high]  -> unknown
          [high+1..n-1]-> 2s

        Time:  O(n)
        Space: O(1)
        """
        n = len(arr)
        low, mid, high = 0, 0, n - 1

        while mid <= high:
            if arr[mid] == 0:
                # put 0 into the 0s region, expand both low and mid
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # 1 is in the correct middle region; just advance
                mid += 1
            else:  # arr[mid] == 2
                # put 2 into the 2s region, shrink high
                # DON'T advance mid; the swapped-in value is unprocessed
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1